import time
from selenium.common.exceptions import NoSuchElementException

def check_add_button(browser):
    try:
        button_add = browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        return False
    return True


def test_exist_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert check_add_button(browser), "Button is not exist!"