from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    # Login locators
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.CSS_SELECTOR, ".login_form .btn")


class ProductPageLocators:
    # Main product locators
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")

    # Alert notifications locators
    SUCCESS_ALERT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BASKET_TOTAL_ALERT = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
