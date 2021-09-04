from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password.send_keys(password)
        conf_password = self.browser.find_element(*LoginPageLocators.REG_CONF_PASSWORD)
        conf_password.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REG_BTN)
        reg_btn.click()


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "LOGIN_EMAIL is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "REG_EMAIL is not found"