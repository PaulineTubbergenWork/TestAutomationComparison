import { test } from '@playwright/test'
import { checkZichtbaarheidEnInhoudVanVeld, englishUrl, openUrlInBrowser, titeltekst, typeInZoekveldEnKlikOpZoeken, welkomsttekst } from '../resources/wikipedia.po'

const zoekterm = "Platypus"

test.describe('Wikipedia', () => {
  test('Checks that I can find the Platypus page on the English Wikipedia', async ({page}) => {
    console.log("Go to the English Wikipedia page")
    await openUrlInBrowser(page, englishUrl)
    console.log("Check that the page is in English")
    await checkZichtbaarheidEnInhoudVanVeld(page, welkomsttekst, 'Welcome to')
    console.log("Search for the Platypus")
    await typeInZoekveldEnKlikOpZoeken(page, zoekterm)
    console.log("Check that the Platypus page was found")
    await checkZichtbaarheidEnInhoudVanVeld(page, titeltekst, zoekterm)
  })

  test('fails on purpose', async ({page}) => {
    console.log("Go to the English Wikipedia page")
    await openUrlInBrowser(page, englishUrl)
    console.log("Check that the page is in English")
    // inhoud tekst is expres fout
    await checkZichtbaarheidEnInhoudVanVeld(page, welkomsttekst, 'Welcom to')
    console.log("Search for the Platypus")
    await typeInZoekveldEnKlikOpZoeken(page, zoekterm)
    console.log("Check that the Platypus page was found")
    await checkZichtbaarheidEnInhoudVanVeld(page, titeltekst, zoekterm)
  })
})