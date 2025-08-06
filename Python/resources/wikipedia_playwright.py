from playwright.sync_api import expect
from resources.wikipedia_variables import search_field, search_button


def open_url_in_browser(page, url):
    page.goto(url)


def check_field_visibility_and_content(page, css_selector, tekst):
    expect(page.locator("css=" + css_selector)).to_contain_text(tekst)


def type_text_in_search_field_and_click_search_button(page, tekst):
    page.locator("css=" + search_field).fill(tekst)
    page.locator("css=" + search_button).click()
