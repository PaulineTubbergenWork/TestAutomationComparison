export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welkomsttekst = 'h1#Welcome_to_Wikipedia'
export const titeltekst = 'h1.firstHeading > span'

export const checkZichtbaarheidEnInhoudVanVeld = (cssSelector, tekst) => {
    cy.get(cssSelector).should('be.visible')
    cy.get(cssSelector).should('contain.text', tekst)
}

export const klikKnopOmZoekveldTeOpenen = () => {
    cy.get('#p-search a').click()
}

export const typeInZoekveldEnKlikOpZoeken = (zoekterm) => {
    const zoekveld = 'input[aria-label="Search Wikipedia"]'
    cy.get(zoekveld).eq(0).type(zoekterm)
    cy.get('form#searchform button').click()
}
