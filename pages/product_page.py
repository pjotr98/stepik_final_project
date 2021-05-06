from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        BasePage.highlight(add_to_basket_btn)
        add_to_basket_btn.click()

    def should_appear_product_in_basket_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        BasePage.highlight(product_name)
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT)
        BasePage.highlight(success_msg)
        assert product_name.text == success_msg.text, "Product's name in alert doesn't equal to added product's name"

    def should_be_equivalent_basket_and_products_totals(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        BasePage.highlight(product_price)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_ALERT)
        BasePage.highlight(basket_total)
        assert product_price.text == basket_total.text, "Basket total in alert doesn't equal to added product's price"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message should disappear after 4 seconds by default"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), \
            "Success message is presented, but should not be"
