from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.wikipedia_variables import search_button, search_field


def open_url_in_browser(browser, url):
    browser.get(url)


def check_field_visibility_and_content(browser, css_selector, text):
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), text)
    )
    assert browser.find_element(By.CSS_SELECTOR, css_selector).is_displayed() == True



def type_text_in_search_field_and_click_search_button(browser, search_term):
    assert browser.find_element(By.CSS_SELECTOR, search_field).is_displayed()
    browser.find_element(By.CSS_SELECTOR, search_field).send_keys(search_term)
    browser.find_element(By.CSS_SELECTOR, search_button).click()

