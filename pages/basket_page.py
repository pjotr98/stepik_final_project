from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), "Msg not visible"

    def should_not_be_products_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ITEM), "Product item appears in basket"
