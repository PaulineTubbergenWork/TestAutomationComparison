from selenium.webdriver.common.by import By
from resources.wikipedia_variables import zoekveld, zoekknop


def open_url_in_browser(browser, url):
    browser.get(url)


def check_zichtbaarheid_en_inhoud_van_veld(browser, css_selector, tekst):
    selector = browser.find_element(By.CSS_SELECTOR, css_selector)
    assert selector.is_displayed() == True
    assert tekst in selector.text



def type_in_zoekveld_en_klik_op_zoeken(browser, zoekterm):
    zoekveld_selector = browser.find_element(By.CSS_SELECTOR, zoekveld)
    assert zoekveld_selector.is_displayed()
    zoekveld_selector.send_keys(zoekterm)
    zoekknop_selector = browser.find_element(By.XPATH, zoekknop)
    zoekknop_selector.click()
