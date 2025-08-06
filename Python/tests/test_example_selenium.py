from selenium import webdriver
from resources.wikipedia_variables import english_url, welcome_text, title_text
from resources.wikipedia_selenium import open_url_in_browser, check_field_visibility_and_content, \
    type_text_in_search_field_and_click_search_button

zoekterm = "Platypus"


def test_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    check_field_visibility_and_content(browser_chrome, welcome_text, "Welcome to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(browser_chrome, zoekterm)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(browser_chrome, title_text, zoekterm)
    browser_chrome.close()


def test_fails_on_purpose():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    # text content is wrong on purpose
    check_field_visibility_and_content(browser_chrome, welcome_text, "Welcom to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(browser_chrome, zoekterm)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(browser_chrome, title_text, zoekterm)
    browser_chrome.close()
