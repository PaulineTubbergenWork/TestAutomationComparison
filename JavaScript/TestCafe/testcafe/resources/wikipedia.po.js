import { Selector } from 'testcafe'

export const englishUrl = 'https://en.wikipedia.org/wiki/Main_Page'
export const welkomsttekst = 'h1#Welcome_to_Wikipedia'
export const titeltekst = 'h1.firstHeading > span'

export const checkZichtbaarheidEnInhoudVanVeld = async (t, cssSelector, tekst) => {
    await t.expect(Selector(cssSelector).visible).eql(true)
    await t.expect(Selector(cssSelector).innerText).contains(tekst)
}

export const typeInZoekveldEnKlikOpZoeken = async (t, zoekterm) => {
    const zoekveld = Selector('input[aria-label="Search Wikipedia"]').nth(0)
    const zoekknop = Selector('form#searchform button')
    await t.typeText(zoekveld, zoekterm)
    await t.click(zoekknop)
}
