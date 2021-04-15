from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError
from utils import UtilsPerson
import datetime, enum, string, random

db = SQLAlchemy()


class Gender(enum.Enum):
    F = 1
    M = 2


class Person(db.Model):
    """ Model representing a person. """

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(150), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    licence_number = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)


class PersonSchema(Schema):
    """ Schema representing a person. This is need for validation"""

    class Meta:
        model = Person
        fields = ("first_name", "middle_name", "last_name", "date_of_birth", "gender")

    first_name = fields.Str(required=True, validate=[validate.Length(min=2, max=100)])
    middle_name = fields.Str(required=False)
    last_name = fields.Str(required=True, validate=[validate.Length(min=2, max=150)])
    date_of_birth = fields.Date(required=True)
    gender = fields.Str(required=True, validate=[validate.OneOf(["M", "F"])])


def create_app():
    # creating flask app with sqlite database
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskproject.db'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/licence", methods=['POST'])
    def create_person():
        create_person_schema = PersonSchema()
        try:
            data = create_person_schema.load(request.get_json())
            licence_number = UtilsPerson.generate_uk_driving_licence_number(data)

            # creating person to add to the db
            new_person = Person(first_name=data["first_name"],
                                middle_name=data["middle_name"],
                                last_name=data["last_name"],
                                date_of_birth=data["date_of_birth"],
                                gender=data["gender"],
                                licence_number=licence_number)

            db.session.add(new_person)
            db.session.commit()
            # returning 13 first characters of licence number
            return licence_number[0:13], 200

        except ValidationError as err:
            error = {
                "status": "error",
                "messages": err.messages
            }
            # return list of errors in json format
            return jsonify(error), 400

    @app.route("/licences", methods=['GET'])
    def get_licences():
        # requirement is to return response in this format ​[“JUDD9507139NP”, “JUDD9507139NP”, “JUDD9507139NP”]
        driving_licences = [item.licence_number for item in Person.query.with_entities(Person.licence_number).all()]
        return jsonify(driving_licences)

    return app


if __name__ == '__main__':
    app = create_app()
    # the app will run on http://0.0.0.0:8080
    app.run(debug=True, host='0.0.0.0', port=8080)
