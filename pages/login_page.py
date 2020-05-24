from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"No login substring in the {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            f"Форма входа отсутствует на {self.browser.current_url}"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            f"Регистрационной формы нет на {self.browser.current_url} странице"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_field.send_keys(email)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        confirm_password_field.send_keys(email)
        click_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        click_button.click()



