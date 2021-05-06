import time
import allure
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    @allure.step("Should be login page")
    def should_be_login_page(self):
        with allure.step("Should be login url"):
            self.should_be_login_url()
        with allure.step("Should be login form"):
            self.should_be_login_form()
        with allure.step("Should be register form"):
            self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "/login" in self.browser.current_url, "Page's URL doesn't have 'login' chunk"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form doesn't present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form doesn't present"

    @staticmethod
    @allure.step("Generate fake email")
    def get_fake_email():
        email = str(time.time()) + "@fakemail.org"
        return email

    @allure.step("Register a new user")
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        BasePage.highlight(register_button)
        register_button.click()
