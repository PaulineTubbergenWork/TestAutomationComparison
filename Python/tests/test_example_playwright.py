from playwright.sync_api import Page, expect
from resources.wikipedia_playwright import open_url_in_browser, check_field_visibility_and_content, \
    type_text_in_search_field_and_click_search_button
from resources.wikipedia_variables import english_url, welcome_text, title_text


search_term = "Platypus"


def test_pw_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia(page: Page):
    print("go to the English Wikipedia page")
    page.goto("https://en.wikipedia.org/wiki/Main_Page")
    print("checks that the page is in English")
    expect(page.locator("css=h1 > span.mw-headline")).to_contain_text("Welcome to")
    print("search for the Platypus")
    page.locator("css=#input[aria-label='Search Wikipedia']").fill("Platypus")
    page.locator("css=form#searchform button").click()
    print("check that the Platypus page was found")
    expect(page.locator("css=h1.firstHeading > span")).to_contain_text("Platypus")


def test_pw_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia_with_custom_functions(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    check_field_visibility_and_content(page, welcome_text, "Welcome to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(page, search_term)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(page, title_text, search_term)


def test_pw_fails_on_purpose(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    # text content is wrong on purpose
    check_field_visibility_and_content(page, welcome_text, "Welcom to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(page, search_term)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(page, titeltekst, search_term)
