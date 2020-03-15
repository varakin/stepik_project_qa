from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    AUTORIZATION_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    AUTORIZATION_PASS = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
