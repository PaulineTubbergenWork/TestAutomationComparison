*** Settings ***
Library     SeleniumLibrary
Resource    ./common.resource


*** Keywords ***
Open url in browser
    [Arguments]    ${url}
    Open browser    ${url}    ${BROWSER_SELENIUM}
    
Check field visibility and content
    [Arguments]    ${css_selector}    ${text}
    Wait Until Keyword Succeeds    10s    1s   Element Text Should Be   ${css_selector}   ${text}
    Wait Until Element Is Visible   ${css_selector}
    
Type text in search field and click search button
    [Arguments]    ${text}
    Wait Until Element Is Visible    ${SEARCH_FIELD}
    Input Text     ${SEARCH_FIELD}    ${text}
    Click Button    ${SEARCH_BUTTON}
