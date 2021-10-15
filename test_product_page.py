from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import pytest
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                    #  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                    #               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                #   ])
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_on_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, page.browser.current_url) #page.browser.current_url
    
    basket.should_be_on_basket_page()
    basket.should_be_no_products_in_basket()
    basket.should_be_empty_basket_message()

@pytest.mark.user_add_prod
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "Password2021")
        page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        prod_name = page.return_product_name()
        prod_price = page.return_product_price()
        page.should_add_product_to_basket(prod_name, prod_price)
   
