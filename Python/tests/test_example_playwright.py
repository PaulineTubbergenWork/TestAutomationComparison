from playwright.sync_api import Page
from resources.wikipedia_playwright import open_url_in_browser, check_zichtbaarheid_en_inhoud_van_veld, \
    type_in_zoekveld_en_klik_op_zoeken
from resources.wikipedia_variables import basic_url, english_url, welkomsttekst, titeltekst

zoekterm = "Platypus"


def test_pw_checks_that_i_can_visit_wikipedia(page: Page):
    open_url_in_browser(page, basic_url)


def test_pw_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    check_zichtbaarheid_en_inhoud_van_veld(page, welkomsttekst, "Welcome to")
    print("search for the Platypus")
    type_in_zoekveld_en_klik_op_zoeken(page, zoekterm)
    print("check that the Platypus page was found")
    check_zichtbaarheid_en_inhoud_van_veld(page, titeltekst, zoekterm)


def test_pw_fails_on_purpose(page: Page):
    print("go to the English Wikipedia page")
    open_url_in_browser(page, english_url)
    print("checks that the page is in English")
    # inhoud tekst is expres fout
    check_zichtbaarheid_en_inhoud_van_veld(page, welkomsttekst, "Welcom to")
    print("search for the Platypus")
    type_in_zoekveld_en_klik_op_zoeken(page, zoekterm)
    print("check that the Platypus page was found")
    check_zichtbaarheid_en_inhoud_van_veld(page, titeltekst, zoekterm)
