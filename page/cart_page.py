from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.base_page import Page


class CartPage(Page):

    EMPTY_CART = (By.CSS_SELECTOR, '.cart-empty.woocommerce-info')

    def verify_empty_cart(self):
        self.verify_text('Your cart is currently empty.', *self.EMPTY_CART)





