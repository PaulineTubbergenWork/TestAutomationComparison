import { test, expect } from '@playwright/test'
import { checkFieldVisibilityAndContent, englishUrl, titleText, welcomeText, openUrlInBrowser, typeTextInSearchFieldAndClickSearchButton } from '../resources/wikipedia.po'

const searchTerm = 'Platypus'

test.describe('Wikipedia', () => {
  test('Checks that I can find the Platypus page on the English Wikipedia', async ({page}) => {
    console.log("Go to the English Wikipedia page")
    await page.goto('https://en.wikipedia.org/wiki/Main_Page')
    console.log("Check that the page is in English")
    await expect(page.locator('css=h1#Welcome_to_Wikipedia')).toBeVisible()
    await expect(page.locator('css=h1#Welcome_to_Wikipedia')).toContainText('Welcome to')
    console.log("Search for the Platypus")
    await page.locator('css=input[aria-label="Search Wikipedia"]').fill('Platypus')
    await page.locator('css=form#searchform button').click()
    console.log("Check that the Platypus page was found")
    await expect(page.locator('css=h1.firstHeading > span')).toBeVisible()
    await expect(page.locator('css=h1.firstHeading > span')).toContainText('Platypus')
  })

  test('Checks that I can find the Platypus page on the English Wikipedia, now with custom functions', async ({page}) => {
    console.log("Go to the English Wikipedia page")
    await openUrlInBrowser(page, englishUrl)
    console.log("Check that the page is in English")
    await checkFieldVisibilityAndContent(page, welcomeText, 'Welcome to')
    console.log("Search for the Platypus")
    await typeTextInSearchFieldAndClickSearchButton(page, searchTerm)
    console.log("Check that the Platypus page was found")
    await checkFieldVisibilityAndContent(page, titleText, searchTerm)
  })

  test('fails on purpose', async ({page}) => {
    console.log("Go to the English Wikipedia page")
    await openUrlInBrowser(page, englishUrl)
    console.log("Check that the page is in English")
    // text content is wrong on purpose
    await checkFieldVisibilityAndContent(page, welcomeText, 'Welcom to')
    console.log("Search for the Platypus")
    await typeTextInSearchFieldAndClickSearchButton(page, searchTerm)
    console.log("Check that the Platypus page was found")
    await checkFieldVisibilityAndContent(page, titleText, searchTerm)
  })
})