from .locators import BasketLocators, CartPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def click_add_to_basket(self):
        link = self.browser.find_element(*BasketLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def success_add_to_basket(self):
        assert self.is_element_present(*BasketLocators.ADDING_SUCCESS), "Товар НЕ добавлен в корзину"
        added_to_basket_text = self.browser.find_element(*BasketLocators.ALERT_ADDED_TO_BASKET).text
        product_name = self.browser.find_element(*BasketLocators.PRODUCT_NAME).text
        assert product_name == added_to_basket_text, \
            f"The alert contains wrong product name: {added_to_basket_text} - {product_name}"

    def should_check_overall_cost(self):
        assert self.is_element_present(
            *BasketLocators.PRODUCT_PRICE), "Product price is not present"
        assert self.is_element_present(*BasketLocators.ALERT_CART_STATUS
                                       ), "No alert with cart status"
        alert_text = self.browser.find_element(
            *BasketLocators.ALERT_CART_STATUS).text.split()[4]
        product_cost = self.browser.find_element(
            *BasketLocators.PRODUCT_PRICE).text.split()[0]
        assert product_cost == alert_text, \
            f"Product cost in cart is not equal to the product cost: {alert_text} != {product_cost}"

    def should_not_see_success_message_after_adding_to_basket(self):
        assert self.is_not_element_present(
            *BasketLocators.ADDING_SUCCESS
        ), "Success element is visible for an user"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*BasketLocators.ADDING_SUCCESS), \
            "Success message is presented, but should not be"

