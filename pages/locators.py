from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    AUTORIZATION_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    AUTORIZATION_PASS = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-primary")

class ProductPageLocators():
    PRODUCT_ADD = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner .col-sm-6.product_main h1")
    PRODUCT_NAME_ADD = (By.CSS_SELECTOR, "#messages .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner .col-sm-6.product_main .price_color")
    PRODUCT_PRICE_ADD = (By.CSS_SELECTOR, "#messages .alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, "#default .header.container-fluid .page_inner .basket-mini.pull-right.hidden-xs .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner .basket-title.hidden-xs div h2")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")