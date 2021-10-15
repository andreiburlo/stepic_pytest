#comment 
import time 
def test_add_to_basket_btn_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    btn = browser.find_element_by_css_selector("#add_to_basket_form")
    assert btn!=None, "The element was not found"
