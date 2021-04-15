# Flask project
This application is responsible for generating and storing in a database UK driving licence numbers 

## Requirements:
1. Create a Flask application running on port 8080
2. The API should have 2 endpoints:
a. POST /licence
i. Request Body:​ {​ “first_name”: str, “middle_name”:
str, “last_name”: str, “date_of_birth”: date
(isoformat), “gender”: str (allowed M|F)}
ii. Response Body: String representing the f​ irst 13​ d​ igits​ of a UK driving licence number using the request body (https://ukdriving.org.uk/licencenumber.html​) e.g.“J​UDD9507139NP”
b. GET /licences
i. Response Body: List of UK driving licence numbers returned
by calls to the previous endpoint e.g.[​“JUDD9507139NP”, “JUDD9507139NP”, “JUDD9507139NP”]
3. Licence numbers should be persisted using SQLAlchemy (underlying DB does not matter)
4. Code must be packaged so it can be easily run on any linux/mac machine. Ideal for this would be docker & docker-compose
5. A basic test suite should be included


## How to run this project
* unpack file flaskproject.zip
* go to the flaskproject folder (if "flaskproject" is the folder you unpacked the files to)
* you need to have docker installed
* run commands: \
``` docker-compose build  ``` \
``` docker-compose up ``` 
* there are two endpoints available \
[GET] http://0.0.0.0:8080/licences \
[POST] http://0.0.0.0:8080/licence 

Sample json for POST endpoint: 
```json
{
"first_name": "Basia",
"middle_name": "Ula",
"last_name": "Smith",
"date_of_birth": "1973-11-05",
"gender": "F"
}
``` 

## Note
* In my opinion this specification https://en.wikipedia.org/wiki/Driving_licence_in_the_United_Kingdom#Driver_numbers is more accurate. 