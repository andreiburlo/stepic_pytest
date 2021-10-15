from .base_page import BasePage
from .locators import ProductPageLocators
import time



class ProductPage(BasePage):

    def return_product_name(self):
        try:
            elm = self.browser.find_element(*ProductPageLocators.PROD_NAME)
        except: 
            print("Product name has not been found")
        return elm.text

    def return_product_price(self):
        elm = self.browser.find_element(*ProductPageLocators.PROD_PRICE)
        return elm.text[1:]

    def return_basket_total(self):
        elm = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)


        return elm.text.split("\n")[0][15:]

    def should_add_product_to_basket(self, prod_name, prod_price):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(1)

        xp = ProductPageLocators.PROD_SCC_MSG.format(prod_name)
        scs_msg = self.browser.find_element_by_xpath(xp)

        basket_total = self.return_basket_total()
        assert scs_msg != None, "There is no success message on product added to basket"
        assert basket_total==prod_price, "Basket total doesn't match with product price"
           
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappear" 

    