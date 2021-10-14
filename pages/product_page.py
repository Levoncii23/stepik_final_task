from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_btn.click()
    
    def should_guest_see_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button not found"

    