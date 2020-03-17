from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.AUTORIZATION_EMAIL), "field autorization login is not presented"
        assert self.is_element_present(*LoginPageLocators.AUTORIZATION_PASS), "field autorization pass is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "field registr login is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASS1), "field registr pass1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASS2), "field registr pass2 is not presented"
