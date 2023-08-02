# Py API Automation Framework Notes

1. In src package non test cases will be present.
    - other than test cases
2. In test_scripts all test cases will be present.
   - crud - in crud packages we write single test cases, 
   basically all CRUD operation or http methods
   - Integration test means all crud methods in one test
   
3. pip list will list all module installed
4.  pip install requests pytest pytest-html faker allure-pytest jsonschema
5. pip freez > requirements.txt
6. pip install requirements.txt
7. for allure report:
`  --alluredir=./allureReports/my_allure_results `
   - navigate to allure report directory
`   allure serve .\allureReports\my_allure_results\`

