**Test automation comparison**

This repo demonstrates the basic use of various e2e test frameworks by letting each framework do the exact same tests: one test without custom functions or variables, one test with custom functions and variables, in part from other files, and one test that fails on purpose so you can check out what a failing test looks like in this framework.

I have written basic steps to get each of the frameworks running. These steps assume you already know git and how a terminal works.

**Steps to run**

First, clone repo. Then follow the steps for the framework you want to get running. The repository is build in such a way that you can get all frameworks running separately.

**JavaScript Frameworks**

Node and npm need to have been installed.

**JavaScript** \
If a package.json already exists, like in this repo, go to the folder of the framework (i.e. Cypress, PlayWright or TestCafe) from inside a terminal and run the following :
<code>npm i</code>

_Installing Cypress if there is no package.json yet_ \
<code>npm install cypress</code> \
note: Cypress expects a lot of extra files and folders, if you don't want those it requires extra configuration. \
Tests folder is called e2e instead of tests because Cypress wants that folder to be called that way. For the same reason the testfiles have .spec.cy.js at the end. You can call them something else but this requires extra setup and configuration.

To run the tests, run
<code>npm run cy:open</code>
This script is defined in the package.json, you can call it something else if you want. cy:open is the script to run the visual testrunner. Run cy:run if you want to run Cypress headlessly. Both commands will run all files in the Cypress/cypress/e2e folder that end in .spec.cy.js.

_Installing JavaScript PlayWright if there is no package.json yet_ \
<code>npm install -D @playwright/test</code> \
install browser so playwright can access browser: \
<code>npx playwright install</code>

To run the tests, run
<code>npm run playwright:tests</code>
This script is defined in the package.json, you can call it something else if you want. playwright-tests is the script to run the visual testrunner. Run playwright-report if you want to run PlayWright headlessly. The current scripts are only running the file wikipedia.spec.js.

_Installing TestCafe if there is no package.json yet_ \
<code>npm install testcafe</code>

To run the tests, run
<code>npm run tc:tests</code>
This script is defined in the package.json, you can call it something else if you want. This script will run the TestCafe tests visually and will stop running without closing the window so you can debug if a test fails.

**Python Frameworks and RobotFramework versions:**

Python version 3.11, from a venv.
(if you open the Python folder in PyCharm, you can let PyCharm create the venv for you. Otherwise search on "how to create a venv". Afterwards, get inside the venv with the command needed for your operating system) \
Pip version 23.3.1, if not up to date: \
<code>pip install --upgrade pip</code> \

Afterwards open the Python or the RobotFramework folder in the terminal from within the venv, and type the following:
<code>pip install -r requirements.txt</code>

_Note if using Selenium for Python or RobotFramework_

Download the Chromedriver that fits the version of Chrome on your computer or pipeline, and your operating system and processor:
https://googlechromelabs.github.io/chrome-for-testing/#stable.
Unpack and place inside the bin-folder of your venv.

_Commands to install Python Selenium with pytest if there is no requirements.txt_ \
<code>pip install pytest</code> \
<code>pip install selenium</code>

You use the command 'pytest' to run the tests. 'pytest --headed' to run the tests in Chrome, and 'pytest tests/test_example_selenium.py --headed' to run a specific test. If running headed, you will briefly see Selenium going though the tests and then see the results in the terminal. If a test fails it will tell you why, but the error might be cryptic.
TODO Selenium is still giving stale element problems

_Commands to install Python PlayWright with pytest if there is no requirements.txt_ \
<code>pip install pytest-playwright</code> \
<code>playwright install</code>

You use the command 'pytest' to run the tests. 'pytest --headed' to run the tests in Chrome, and 'pytest tests/test_example_playwright.py --headed' to run a specific test. If running headed, you will briefly see PlayWright going though the tests and then see the results in the terminal. If a test fails it will tell you why, but the error might be cryptic.

_Commands to install RobotFramework Selenium if there is no requirements.txt_ \
<code>pip install robotframework</code> \
<code>pip install --upgrade robotframework-seleniumlibrary</code> \

To run the tests, run the following command from the RFSelenium folder:
<code>robot .</code>
(or 'robot example_selenium.robot' to run a specific file).
The browser will popup and go through the tests, the results will be shown in the terminal. Selenium will make screenshots of things that go wrong. You can look the results up in more detail in an html-report made by RobotFramework.

_Commands to RobotFramework PlayWright if there is no requirements.txt_ \
<code>pip install robotframework-browser</code> \
<code>rfbrowser init</code>

To run the tests, run 'rfbrowser init' from the RFPlaywright folder if you used installed the requirements.txt.
Then run the tests with the following command:
<code>robot .</code>
(or 'robot example_playwright.robot' to run a specific file).
The browser will popup and go through the tests, the results will be shown in the terminal. Playwright will make screenshots of things that go wrong. You can look the results up in more detail in an html-report made by RobotFramework.

**TODO**
RobotFramework reports currently aren't landing in one folder, need to find a way to do this.
Add poetry?
Add docker?
Add pipeline?

**Flaky tests, possibly need a different demo website**
Wikipedia has changed since I first wrote these tests and now they are sometimes flaky. Haven't found a solution yet.

These are possible demo website, but most of them have some kind of problem during automation:
https://petstore.swagger.io/ \
https://www.demoblaze.com/ \
https://parabank.parasoft.com/parabank/index.htm \
https://www.saucedemo.com/ \
https://petstore.octoperf.com/actions/Catalog.action \
https://github.com/cypress-io/cypress-realworld-app
