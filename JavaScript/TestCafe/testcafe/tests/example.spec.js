import { checkZichtbaarheidEnInhoudVanVeld, welkomsttekst, typeInZoekveldEnKlikOpZoeken, titeltekst, basicUrl, klikKnopOmZoekveldTeOpenen } from "../resources/wikipedia.po"
import { Selector } from 'testcafe'

const zoekterm = 'Platypus'

fixture('Getting Started')
    .page(basicUrl);

test('Checks that I can visit Wikipedia', async t => {
    console.log('test has been reached');
});

fixture('Wikipedia')
    .page('https://en.wikipedia.org/wiki/Main_Page')

test('Checks that I can find the Platypus page on the English Wikipedia', async t => {
    console.log("Go to the English Wikipedia page")

    console.log("Check that the page is in English")
    await t.expect(Selector('h1#Welcome_to_Wikipedia').visible).eql(true)
    await t.expect(Selector('h1#Welcome_to_Wikipedia').innerText).contains('Welcome to')

    console.log("Search for the Platypus")
    await t.typeText(Selector('input[aria-label="Search Wikipedia"]').nth(0), 'Platypus')
    await t.click(Selector('form#searchform button'))

    console.log("Check that the Platypus page was found")
    await t.expect(Selector('h1.firstHeading > span').visible).eql(true)
    await t.expect(Selector('h1.firstHeading > span').innerText).contains('Platypus')
})

test('Checks that I can find the Platypus page on the English Wikipedia, now with custom functions', async t => {
    console.log("Go to the English Wikipedia page")
    console.log("Check that the page is in English")
    await checkZichtbaarheidEnInhoudVanVeld(t, welkomsttekst, 'Welcome to')
    console.log("Search for the Platypus")
    await typeInZoekveldEnKlikOpZoeken(t, zoekterm)
    console.log("Check that the Platypus page was found")
    await checkZichtbaarheidEnInhoudVanVeld(t, titeltekst, zoekterm)
})

test('Fails on purpose', async t => {
    console.log("Go to the English Wikipedia page")
    console.log("Check that the page is in English")
    // inhoud tekst is expres fout
    await checkZichtbaarheidEnInhoudVanVeld(t, welkomsttekst, 'Welcom to')
    console.log("Search for the Platypus")
    await typeInZoekveldEnKlikOpZoeken(t, zoekterm)
    console.log("Check that the Platypus page was found")
    await checkZichtbaarheidEnInhoudVanVeld(t, titeltekst, zoekterm)
})
