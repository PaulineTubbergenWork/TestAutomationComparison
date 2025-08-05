import { expect } from '@playwright/test'

export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welkomsttekst = 'css=h1 > span.mw-headline'
export const titeltekst = 'css=h1.firstHeading > span'

export const openUrlInBrowser = async (page, url) => await page.goto(url)

export const checkZichtbaarheidEnInhoudVanVeld = async (page, cssSelector, tekst) => {
    await expect(page.locator(cssSelector)).toBeVisible()
    await expect(page.locator(cssSelector)).toContainText(tekst)
}

export const typeInZoekveldEnKlikOpZoeken = async (page, zoekterm) => {
    const zoekveld = 'css=#searchInput[aria-label="Search Wikipedia"]'
    const zoekknop = "xpath=//button[text()='Search']"
    await page.locator(zoekveld).fill(zoekterm)
    await page.locator(zoekknop).click()
}
