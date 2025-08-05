import { Selector } from 'testcafe'

export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welcomeText = 'h1#Welcome_to_Wikipedia'
export const titleText = 'h1.firstHeading > span'

export const checkFieldVisibilityAndContent = async (t, cssSelector, text) => {
    await t.expect(Selector(cssSelector).visible).eql(true)
    await t.expect(Selector(cssSelector).innerText).contains(text)
}

export const typeTextInSearchFieldAndClickSearchButton = async (t, searchTerm) => {
    const searchField = Selector('input[aria-label="Search Wikipedia"]').nth(0)
    const searchButton = Selector('form#searchform button')
    await t.typeText(searchField, searchTerm)
    await t.click(searchButton)
}
