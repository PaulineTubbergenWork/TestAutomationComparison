import { checkFieldVisibilityAndContent, clickButtonToOpenSearchField, englishUrl, titleText, typeTextInSearchFieldAndClickSearchButton, welcomeText } from '../resources/wikipedia.po'

const searchTerm = 'Platypus'

describe('Wikipedia', () => {
  beforeEach(() => {
    cy.log('go to the English Wikipedia page')
    cy.visit(englishUrl)
  })

  it('checks that I can find the Platypus page on the English Wikipedia', () => {
    cy.log('check that the page is in English')
    cy.get('h1#Welcome_to_Wikipedia').should('be.visible')
    cy.get('h1#Welcome_to_Wikipedia').should('contain.text', 'Welcome to')

    cy.log('search for the Platypus')
    cy.get('#p-search a').click()
    cy.get('input[aria-label="Search Wikipedia"]').eq(0).type('Platypus')
    cy.get('form#searchform button').click()

    cy.log('check that the Platypus page was found')
    cy.get('h1.firstHeading > span').should('be.visible')
    cy.get('h1.firstHeading > span').should('contain.text', 'Platypus')
  })

  it('checks that I can find the Platypus page on the English Wikipedia, now with custom functions', () => {
    cy.log('check that the page is in English')
    checkFieldVisibilityAndContent(welcomeText, 'Welcome to')
    cy.log('search for the Platypus')
    clickButtonToOpenSearchField()
    typeTextInSearchFieldAndClickSearchButton(searchTerm)
    cy.log('check that the Platypus page was found')
    checkFieldVisibilityAndContent(titleText, searchTerm)
  })

  it('fails on purpose', () => {
    cy.log('check that the page is in English')
    // inhoud tekst is wrong on purpose
    checkFieldVisibilityAndContent(welcomeText, 'Welcom to')
    cy.log('search for the Platypus')
    clickButtonToOpenSearchField()
    typeTextInSearchFieldAndClickSearchButton(searchTerm)
    cy.log('check that the Platypus page was found')
    checkFieldVisibilityAndContent(titleText, searchTerm)
  })
})
