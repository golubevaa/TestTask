# Test Scenario \#1 from https://www.automationexercise.com/test_cases

### Set up
Installed python3 is required (I used 3.11.2) 
1. Download project
2. Go to TestTask folder 
3. Create virtual environment
4. Execute in command line:
```commandline
pip install -r requirements.txt
playwright install
pytest tests/logingTest.py
```

### Allure results
Installed allure is required (see https://allurereport.org/docs/install/)
Execute for build allure report 
```commandline
allure serve allure-results
```

### Additional details
* Test running via chromium by default.
* Set environment variable BROWSER = 'firefox' to run tests via firefox
* Set environment variable HEADLESS = True to run test in headless mode
* Default actions timeout = 10 sec