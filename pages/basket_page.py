from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_PRODUCT_IN_BASKET), "product in basket"

    def should_text_about_empty_basket(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text, \
            "basket is not empty"
