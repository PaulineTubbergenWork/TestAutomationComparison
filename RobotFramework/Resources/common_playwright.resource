*** Settings ***
Library     Browser
Resource    ./common.resource

*** Variables ***
${HEADLESS}                 False

*** Keywords ***
Open url in browser
    [Arguments]     ${url}
    New Browser     ${BROWSER_PLAYWRIGHT}     ${HEADLESS}
    New Page        ${url}

Check field visibility and content
    [Arguments]    ${css_selector}    ${text}
    Get Element States    ${css_selector}    validate    visible
    Get Text    ${css_selector}    ==    ${text}

Type text in search field and click search button
    [Arguments]    ${text}
    Type Text    ${SEARCH_FIELD}    ${text}
    Click    ${SEARCH_BUTTON}
