from .base_page import BasePage
from .locators import CartPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *CartPageLocators.FREE_BASKET), "Basket is not empty"

    def should_contain_empty_text(self):
        empty_text = "Your basket is empty"
        assert self.is_element_present(
            *CartPageLocators.EMPTY_BASKET
        ), "Cart empty warning element is not present on the page"
        assert self.is_text_present(
            *CartPageLocators.EMPTY_BASKET, empty_text
        ), f"The text '{empty_text}' is not present in the empty basket warning element"
