# Python API Automation Framework

## Integration test cases for the Restful Booker

URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. GET, POST, PUT, PATCH, DELETE 
2. Response Body, Headers, Status code.
2. Auth - Basic Auth , Cookie Auth
3. JSON Schemas Validation.


### Tech Stack (PythonPackages used)

1. Python, Request module
2. Pytest, Pytest-html
3. Allure Report
4. Faker, CSV, JSON, YAML
5. Run via command line --Jenkins


### P.S - DB Connection (In future)

## list all module installed
` pip install requests pytest pytest-html faker allure-pytest jsonschema`


### How to run via Jenkins

### How to run locally and see the report?
 for allure report:
`  --alluredir=./allureReports/my_allure_results `
   - navigate to allure report directory

`   allure serve .\allureReports\my_allure_results\ `