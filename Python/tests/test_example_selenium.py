from selenium import webdriver
from resources.wikipedia_variables import basic_url, english_url, welkomsttekst, titeltekst
from resources.wikipedia_selenium import open_url_in_browser, check_zichtbaarheid_en_inhoud_van_veld, \
    type_in_zoekveld_en_klik_op_zoeken

zoekterm = "Platypus"


def test_checks_that_i_can_visit_wikipedia():
    browser_chrome = webdriver.Chrome()
    open_url_in_browser(browser_chrome, basic_url)
    browser_chrome.close()


def test_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    check_zichtbaarheid_en_inhoud_van_veld(browser_chrome, welkomsttekst, "Welcome to")
    print("search for the Platypus")
    type_in_zoekveld_en_klik_op_zoeken(browser_chrome, zoekterm)
    print("check that the Platypus page was found")
    check_zichtbaarheid_en_inhoud_van_veld(browser_chrome, titeltekst, zoekterm)
    browser_chrome.close()


def test_fails_on_purpose():
    browser_chrome = webdriver.Chrome()
    print("go to the English Wikipedia page")
    open_url_in_browser(browser_chrome, english_url)
    print("checks that the page is in English")
    # inhoud tekst is expres fout
    check_zichtbaarheid_en_inhoud_van_veld(browser_chrome, welkomsttekst, "Welcom to")
    print("search for the Platypus")
    type_in_zoekveld_en_klik_op_zoeken(browser_chrome, zoekterm)
    print("check that the Platypus page was found")
    check_zichtbaarheid_en_inhoud_van_veld(browser_chrome, titeltekst, zoekterm)
    browser_chrome.close()
