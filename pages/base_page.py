import math
import time
import allure
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    @staticmethod
    def highlight(element):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element.parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(4, "red"))
        time.sleep(0.4)
        apply_style(original_style)

    @allure.step("Open app")
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        with allure.step(f"Check is element present. find element '{what}' by '{how}'"):
            try:
                element = self.browser.find_element(how, what)
                BasePage.highlight(element)
            except NoSuchElementException:
                return False
            return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            element = WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
            BasePage.highlight(element)
        except TimeoutException:
            return False
        return True

    @allure.step("Solving quiz")
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    @allure.step("Go to login page")
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        BasePage.highlight(login_link)
        login_link.click()

    @allure.step("Go to basket page")
    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        BasePage.highlight(basket)
        basket.click()

    @allure.step("Should be login link")
    def should_be_login_link(self):
        element = self.is_element_present(*BasePageLocators.LOGIN_LINK)
        assert element, "Login link isn't presented"

    @allure.step("Should be authorized user")
    def should_be_authorized_user(self):
        element = self.is_element_present(*BasePageLocators.USER_ICON)
        assert element, "User icon is not presented, probably unauthorised user"

