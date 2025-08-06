from selenium import webdriver
from selenium.webdriver.common.by import By
from resources.wikipedia_variables import english_url, welcome_text, title_text
from resources.wikipedia_selenium import open_url_in_browser, check_field_visibility_and_content, \
    type_text_in_search_field_and_click_search_button

search_term = "Platypus"


def test_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    browser_chrome.get("https://en.wikipedia.org/wiki/Main_Page")
    print("checks that the page is in English")
    selector = browser_chrome.find_element(By.CSS_SELECTOR, "h1 > span.mw-headline")
    assert selector.is_displayed() == True
    assert "Welcome to" in selector.text
    print("search for the Platypus")
    assert browser_chrome.find_element(By.CSS_SELECTOR, "#input[aria-label='Search Wikipedia']").is_displayed()
    browser_chrome.find_element(By.CSS_SELECTOR, "#input[aria-label='Search Wikipedia']").send_keys("Platypus")
    browser_chrome.find_element(By.CSS_SELECTOR, "form#searchform button").click()
    print("check that the Platypus page was found")
    assert browser_chrome.find_element(By.CSS_SELECTOR, "h1.firstHeading > span").is_displayed() == True
    assert "Platypus" in browser_chrome.find_element(By.CSS_SELECTOR, "h1.firstHeading > span").text
    browser_chrome.close()


def test_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia_with_custom_functions():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    check_field_visibility_and_content(browser_chrome, welcome_text, "Welcome to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(browser_chrome, search_term)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(browser_chrome, title_text, search_term)
    browser_chrome.close()


def test_fails_on_purpose():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    # text content is wrong on purpose
    check_field_visibility_and_content(browser_chrome, welcome_text, "Welcom to")
    print("search for the Platypus")
    type_text_in_search_field_and_click_search_button(browser_chrome, search_term)
    print("check that the Platypus page was found")
    check_field_visibility_and_content(browser_chrome, title_text, search_term)
    browser_chrome.close()
