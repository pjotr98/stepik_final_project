import allure

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    @allure.step("Should be 'empty basket' message")
    def should_be_empty_basket_message(self):
        element = self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG)
        assert element, "Msg not visible"

    @allure.step("Should not be products items in basket")
    def should_not_be_products_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ITEM), "Product item appears in basket"
