from playwright.sync_api import Page
from resources.wikipedia_playwright import open_url_in_browser, check_field_visibility_and_content, \
    type_text_in_search_field_and_click_search_button
from resources.wikipedia_variables import english_url, welcome_text, title_text

zoekterm = "Platypus"

def test_pw_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    check_field_visibility_and_content(page, welcome_text, "Welcome to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(page, zoekterm)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(page, title_text, zoekterm)


def test_pw_fails_on_purpose(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    # text content is wrong on purpose
    check_field_visibility_and_content(page, welcome_text, "Welcom to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(page, zoekterm)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(page, titeltekst, zoekterm)
