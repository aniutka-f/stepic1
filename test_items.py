import pytest
import time
from selenium.webdriver.common.by import By
import time

links = [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
    'http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/'
]

@pytest.mark.parametrize('link', links)
def test_find_add_to_basket_button(browser, link):
    browser.get(link)
    curr_language = browser.execute_script('return window.navigator.language || window.navigator.userLanguage')
    if 'fr' in curr_language:
        time.sleep(30)
    find_buttons = browser.find_elements(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert find_buttons, f"Basket button is absent"
