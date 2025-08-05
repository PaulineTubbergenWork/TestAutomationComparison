from playwright.sync_api import expect
from resources.wikipedia_variables import zoekveld, zoekknop


def open_url_in_browser(page, url):
    page.goto(url)


def check_zichtbaarheid_en_inhoud_van_veld(page, css_selector, tekst):
    expect(page.locator("css=" + css_selector)).to_contain_text(tekst)


def type_in_zoekveld_en_klik_op_zoeken(page, tekst):
    page.locator("css=" + zoekveld).fill(tekst)
    page.locator("xpath=" + zoekknop).click()
