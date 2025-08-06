*** Settings ***
Documentation      Example suite
Resource           ../../Resources/common_playwright.resource

*** Variables ***
${SEARCH_TERM}    Platypus

*** Test Cases ***
Check that I can find the Platypus page on the English Wikipedia
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
