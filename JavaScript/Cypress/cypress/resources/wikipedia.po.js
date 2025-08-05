export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welcomeText = 'h1#Welcome_to_Wikipedia'
export const titleText = 'h1.firstHeading > span'

export const checkFieldVisibilityAndContent = (cssSelector, tekst) => {
    cy.get(cssSelector).should('be.visible')
    cy.get(cssSelector).should('contain.text', tekst)
}

export const clickButtonToOpenSearchField = () => {
    cy.get('#p-search a').click()
}

export const typeTextInSearchFieldAndClickSearchButton = (zoekterm) => {
    const searchTerm = 'input[aria-label="Search Wikipedia"]'
    cy.get(searchTerm).eq(0).type(zoekterm)
    cy.get('form#searchform button').click()
}
