from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = LoginPageLocators.LOGIN_URL 
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_see_login_form(browser):
    link = LoginPageLocators.LOGIN_URL 
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_see_registartion_form(browser):
    link = LoginPageLocators.LOGIN_URL  
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()