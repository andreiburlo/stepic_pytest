from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") 

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") 
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONF_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")


class ProductPageLocators():
    PROD_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PROD_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PROD_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(., 'has been added')] /strong")

    PROD_SCC_MSG = """//div[@id='messages']//strong[text()="{}"]"""


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BTN = (By.XPATH, "//a[text()='View basket']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[contains(text(), 'Your basket is empty')]")
    ITEMS_TO_BUY_NOW_MESSAGE = (By.XPATH, "//h2[text()='Items to buy now']")
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, ".basket_summary")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

