from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_appear_product_in_basket_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT).text
        assert product_name == success_msg, "Product's name in alert doesn't equal to added product's name"

    def should_be_equivalent_basket_and_products_totals(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_ALERT).text
        assert product_price == basket_total, "Basket total in alert doesn't equal to added product's price"
