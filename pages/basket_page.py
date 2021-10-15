from .base_page import BasePage
from .locators import BasePageLocators



class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
            assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "there is no empty basket meassage"

    def should_be_no_products_in_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_ITEMS_LIST)==False, "There is product in basket"
 
    def should_be_on_basket_page(self):
        assert "/basket/" in self.browser.current_url, "It is not a basket page"