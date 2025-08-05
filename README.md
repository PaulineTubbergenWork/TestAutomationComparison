**Stappen om werkend te krijgen**

Python versie 3.11, in venv
(automatisch aangemaakt bij openen project in PyCharm, Python en RobotFramework hebben ieder een aparte venv nodig). \
Pip versie 23.3.1, als nog niet up-to-date: \
<code>pip install --upgrade pip</code> \
Node versie 21.1.0. \
Npm versie 10.2.0.

**RobotFramework Selenium** \
<code>pip install robotframework</code> \
<code>pip install --upgrade robotframework-seleniumlibrary</code> \
En download the arm-chromedriver die overeenkomt met de versie van
Chrome op je computer:
https://googlechromelabs.github.io/chrome-for-testing/#stable.
Pak uit en plaats in de bin-map van je venv.

**RobotFramework PlayWright** \
<code>pip install robotframework-browser</code> \
<code>rfbrowser init</code>

**Python Selenium met pytest** \
<code>pip install pytest</code> \
<code>pip install selenium</code>
En download the arm-chromedriver die overeenkomt met de versie van
Chrome op je computer:
https://googlechromelabs.github.io/chrome-for-testing/#stable.
Pak uit en plaats in de bin-map van je venv.

**Python PlayWright met pytest** \
<code>pip install pytest-playwright</code> \
<code>playwright install</code>

**JavaScript** \
Normaliter commando's hieronder, nu naar ieder testframework zijn map navigeren en
<code>npm i</code> doen, omdat package.json al aanwezig.

**JavaScript Cypress** \
<code>npm install cypress</code> \
noot: er zijn nogal wat extra files hier omdat Cypress die verwacht, moet je configuren als je die niet wilt. \
tests heten e2e ipv tests omdat dat ook iets is wat Cypress verwacht, idem de 'cy' tussen 'spec' en 'js'

**JavaScript PlayWright** \
<code>npm i -D @playwright/test</code> \
installeren van browsers: \
<code>npx playwright install</code>

**JavaScript TestCafe** \
<code>npm install testcafe</code>

**TODO**
Manier vinden om RobotFramework rapportage-bestanden in nette map te stoppen in plaats van overal verspreid.
Poetry toevoegen?
Docker toevoegen?
Dingen zijn nu afwisselend Engels en Nederlands, dat is onhandig. Fixen.

**TODO**
Wikipedia heeft zichzelf in de tussentijd aangepast, en test is nu flaky zelfs na aanpassingen door raar gedrag zoekknop.
Cypress en TestCafe al aangepast, rest nog niet.
Mogelijk tests op demowebsite richten ipv wikipedia, meer zekerheid dat dit hetzelfde blijft?
Mogelijke demowebsites:
https://petstore.swagger.io/ \
https://www.demoblaze.com/ \
https://parabank.parasoft.com/parabank/index.htm \
https://www.saucedemo.com/ \
https://petstore.octoperf.com/actions/Catalog.action \
https://github.com/cypress-io/cypress-realworld-app
