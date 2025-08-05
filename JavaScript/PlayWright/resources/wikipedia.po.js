import { expect } from '@playwright/test'

export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welcomeText = 'css=h1#Welcome_to_Wikipedia'
export const titleText = 'css=h1.firstHeading > span'

export const openUrlInBrowser = async (page, url) => await page.goto(url)

export const checkFieldVisibilityAndContent = async (page, cssSelector, text) => {
    await expect(page.locator(cssSelector)).toBeVisible()
    await expect(page.locator(cssSelector)).toContainText(text)
}

export const clickButtonToOpenSearchField = async (page) => {
    await page.locator('#p-search a').click();
}

export const typeTextInSearchFieldAndClickSearchButton = async (page, searchTerm) => {
    const searchField = 'css=input[aria-label="Search Wikipedia"]'
    const searchButton = 'css=form#searchform button'
    await page.locator(searchField).fill(searchTerm)
    await page.locator(searchButton).click()
}
