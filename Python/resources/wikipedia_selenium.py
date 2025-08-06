from selenium.webdriver.common.by import By
from resources.wikipedia_variables import search_button, search_field


def open_url_in_browser(browser, url):
    browser.get(url)


def check_field_visibility_and_content(browser, css_selector, tekst):
    selector = browser.find_element(By.CSS_SELECTOR, css_selector)
    assert selector.is_displayed() == True
    assert tekst in selector.text


def type_text_in_search_field_and_click_search_button(browser, search_term):
    search_field_selector = browser.find_element(By.CSS_SELECTOR, search_field)
    assert search_field_selector.is_displayed()
    search_field_selector.send_keys(search_term)
    search_button_selector = browser.find_element(By.CSS_SELECTOR, search_button)
    search_button_selector.click()
