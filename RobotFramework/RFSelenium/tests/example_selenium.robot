*** Settings ***
Documentation    Example suite
Resource        ../../Resources/common_selenium.resource

*** Variables ***
${SEARCH_TERM}    Platypus

*** Test Cases ***
Check that I can find the Platypus page on the English Wikipedia
    Log    Go to the English Wikipedia page
    Open browser    https://en.wikipedia.org/wiki/Main_Page    Chrome
    Log    Check that the page is in English
    Wait Until Element Is Visible   css=h1#Welcome_to_Wikipedia
    Element Text Should Be   css=h1#Welcome_to_Wikipedia    Welcome to Wikipedia
    Log    Search for the platypus
    Wait Until Element Is Visible    css=input[aria-label="Search Wikipedia"]
    Input Text     css=input[aria-label="Search Wikipedia"]    Platypus
    Click Button    css=form#searchform button
    Log    Check that the platypus page was found
    Wait Until Keyword Succeeds    10s    1s   Element Text Should Be     css=h1.firstHeading > span    Platypus
    Wait Until Element Is Visible   css=h1.firstHeading > span

Check that I can find the Platypus page on the English Wikipedia, now with keywords
    Log    Go to the English Wikipedia page
    Open Url In Browser    ${ENGLISH_URL}
    Log    Check that the page is in English
    Check field visibility and content    ${WELCOME_TEXT}    Welcome to Wikipedia
    Log    Search for the platypus
    Type text in search field and click search button    ${SEARCH_TERM}
    Log    Check that the platypus page was found
    Check field visibility and content    ${TITLE_TEXT}    ${SEARCH_TERM}
    
Check what a failed test looks like
    Log    Go to the English Wikipedia page
    Open Url In Browser    ${ENGLISH_URL}
    Log    Check that the page is in English
    # text content is wrong on purpose
    Check field visibility and content    ${WELCOME_TEXT}    Welcom to Wikipedia
    Log    Search for the platypus
    Type text in search field and click search button   ${SEARCH_TERM}
    Log    Check that the platypus page was found
    Check field visibility and content    ${TITLE_TEXT}    ${SEARCH_TERM}

