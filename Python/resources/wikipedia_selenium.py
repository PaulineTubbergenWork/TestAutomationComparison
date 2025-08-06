from selenium.webdriver.common.by import By
from resources.wikipedia_variables import search_button, search_field


def open_url_in_browser(browser, url):
    browser.get(url)


def check_field_visibility_and_content(browser, css_selector, tekst):
    selector = browser.find_element(By.CSS_SELECTOR, css_selector)
    assert selector.is_displayed() == True
    assert tekst in selector.text


def type_text_in_search_field_and_click_search_button(browser, zoekterm):
    zoekveld_selector = browser.find_element(By.CSS_SELECTOR, search_field)
    assert zoekveld_selector.is_displayed()
    zoekveld_selector.send_keys(zoekterm)
    zoekknop_selector = browser.find_element(By.CSS_SELECTOR, search_button)
    zoekknop_selector.click()
