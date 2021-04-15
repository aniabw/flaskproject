import pytest, json
from app import Person, create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def mock_person_model():
    my_model = Person(
        id=1,
        first_name="Basia",
        middle_name="Ula",
        last_name="Smith",
        date_of_birth="1973-11-05",
        gender="F",
        licence_number="SMITH761053BU",
        created_at="2021-03-07 13:24:51"
    )
    return my_model


def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def test_person_model_mock(mock_person_model):
    """
    GIVEN a Person model
    WHEN a new Person with licence number is created
    THEN check the id, first_name, middle_name, last_name, date_of_birth, gender, licence_number, created_at fields are defined correctly
    """

    person_model = mock_person_model

    assert person_model.id == 1
    assert person_model.first_name == 'Basia'
    assert person_model.middle_name == 'Ula'
    assert person_model.last_name == 'Smith'
    assert person_model.date_of_birth == '1973-11-05'
    assert person_model.gender == 'F'
    assert person_model.licence_number == 'SMITH761053BU'
    assert person_model.created_at == '2021-03-07 13:24:51'


def test_get_licences_response(app):
    client = app.test_client()
    response = client.get('/licences')
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert type(response_data) == list


def test_create_person_response(app):
    response = post_json(app.test_client(), '/licence', {"first_name": "Basia",
                                                         "middle_name": "Ula",
                                                         "last_name": "Smith",
                                                         "date_of_birth": "1973-11-05",
                                                         "gender": "F"
                                                         })

    response_data = response.data.decode()

    assert response.status_code == 200
    assert response_data == 'SMITH761053BU'
    assert len(response_data) == 13