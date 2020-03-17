from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_product(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_ADD).click()

    def calculate_code(self):
        self.solve_quiz_and_get_code()

    def check_name_price(self):
        name_book = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price_book = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD).text == name_book, "name of book different"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADD).text == price_book, "price book differernt"




