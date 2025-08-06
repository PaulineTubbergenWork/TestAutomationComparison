*** Settings ***
Library     SeleniumLibrary
Resource    ./common.resource


*** Keywords ***
Open url in browser
    [Arguments]    ${url}
    Open browser    ${url}    ${BROWSER_SELENIUM}
    
Check field visibility and content
    [Arguments]    ${css_selector}    ${text}
    Element Should Be Visible   ${css_selector}
    Element Text Should Be   ${css_selector}    ${text}
    
Type text in search field and click search button
    [Arguments]    ${text}
    Input Text     ${SEARCH_FIELD}    ${text}
    Click Button    ${SEARCH_BUTTON}
