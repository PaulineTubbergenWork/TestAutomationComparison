*** Settings ***
Documentation      Example suite
Resource           ../../Resources/common_playwright.resource

*** Variables ***
${SEARCH_TERM}    Platypus

*** Test Cases ***
Check that I can find the Platypus page on the English Wikipedia
    Log    Go to the English Wikipedia page
    New Browser     Chromium     False
    New Page        https://en.wikipedia.org/wiki/Main_Page
    Log    Check that the page is in English
    Get Element States    css=h1#Welcome_to_Wikipedia    validate    visible
    Get Text    css=h1#Welcome_to_Wikipedia    ==    Welcome to Wikipedia
    Log    Search for the platypus
    Type Text    css=input[aria-label="Search Wikipedia"]    Platypus
    Click    css=form#searchform button
    Log    Check that the platypus page was found
    Get Element States    css=h1.firstHeading > span    validate    visible
    Get Text    css=h1.firstHeading > span    ==    Platypus

Check that I can find the Platypus page on the English Wikipedia, now with custom key words
    Log    Go to the English Wikipedia page
    Open Url In Browser    ${ENGLISH_URL}
    Log    Check that the page is in English
    Check field visibility and content    ${WELCOME_TEXT}    Welcome to Wikipedia
    Log    Search for the platypus
    Type text in search field and click search button      ${SEARCH_TERM}
    Log    Check that the platypus page was found
    Check field visibility and content    ${TITLE_TEXT}    ${SEARCH_TERM}
    
Check what a failed test looks like
    Log    Go to the English Wikipedia page
    Open Url In Browser    ${ENGLISH_URL}
    Log    Check that the page is in English
    # text content is wrong on purpose
    Check field visibility and content    ${WELCOME_TEXT}    Welcom to Wikipedia
    Log    Search for the platypus
    Type text in search field and click search button    ${SEARCH_TERM}
    Log    Check that the platypus page was found
    Check field visibility and content    ${TITLE_TEXT}    ${SEARCH_TERM}
