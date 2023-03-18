from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert basket_button, f"Basket button is absent"