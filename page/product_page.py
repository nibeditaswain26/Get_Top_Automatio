from selenium.webdriver.common.by import By
from page.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ProductPage(Page):
    ipad_mini_left_right_arrow = (By.CSS_SELECTOR, 'ul[class="next-prev-thumbs is-small nav-right text-right"] li')
    IPAD_DROP_DOWN = (By.CSS_SELECTOR, '#menu-item-470 li')
    USER_RATTING = (By.CSS_SELECTOR, '.woocommerce-product-rating')
    CLICK_ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.single_add_to_cart_button.button')
    ORIGINAL_PRODUCT_PRICE = (By.CSS_SELECTOR, 'p[class="price product-page-price price-on-sale"] ins '
                                               'span[class="woocommerce-Price-amount amount"]')
    EXPECTED_PRICE_TOP_NAV_MENU = (By.CSS_SELECTOR, 'span[class="cart-price"] span[class="woocommerce-Price-amount amount"]')
    ACTUAL_AMOUNT_TOP_NAV_MENU = (By.CSS_SELECTOR, 'a[class="header-cart-link is-small"] strong')
    EXPECTED_AMOUNT_PRODUCT_PAGE = (By.NAME, 'quantity')
    ORIGINAL_PRODUCT_NAME = (By.CSS_SELECTOR, 'h1[class="product-title product_title entry-title"]')
    EXPECTED_PRODUCT_NAME = (By.XPATH, '//div[contains(@class,"flex-col hide-for-medium flex-right")]//a[contains'
                                       '(@href,"https://gettop.us/product/macbook-pro-13/")]')
    SUBTOTAL_PRICE = (By.CSS_SELECTOR, 'span[class="cart-price"] span[class="woocommerce-Price-amount amount"]')
    VIEW_CART_BTN = (By.CSS_SELECTOR, 'li[class="html widget_shopping_cart"] a[class="button wc-forward"]')
    CHECK_OUT_BTN = (By.CSS_SELECTOR, 'li[class="html widget_shopping_cart"] a[class="button checkout wc-forward"]')
    CROSS_SYMBOL_ICON = (By.CSS_SELECTOR, '.remove.remove_from_cart_button')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'li[class="html widget_shopping_cart"] p')

    def verify_product_page(self, product_page):
        self.verify_url_contains_query(product_page)

    def verify_left_right_arrow(self):
        """
        ipad_all_drop_down_btn = self.find_elements(*self.IPAD_DROP_DOWN) #[ele1, ele2, ele3, ele4]

        for btn in range(len(ipad_all_drop_down_btn)):
            if btn == (len(ipad_all_drop_down_btn)-1):
                expected_arrow_count = 1

            else:
                expected_arrow_count = 2

         ipad_all_drop_down_btn[btn].click()
         """
        expected_arrow_count = 2
        actual_arrow_count = len(self.find_elements(*self.ipad_mini_left_right_arrow))
        assert actual_arrow_count == expected_arrow_count, f'Expected {expected_arrow_count} ' \
                                                                   f'but got {actual_arrow_count} arrow count'

    def verify_user_ratting(self):
        self.find_element(*self.USER_RATTING)
        print('User rating is not present.')

    def click_add_to_product(self):
        self.find_element(*self.CLICK_ADD_TO_CART_BTN).click()

    def verify_price(self):
        original_product_price = self.find_element(*self.ORIGINAL_PRODUCT_PRICE).text
        actual_product_price = self.find_element(*self.EXPECTED_PRICE_TOP_NAV_MENU).text
        assert original_product_price == actual_product_price, 'original price and actual price not same.'

    def verify_amount_of_product(self):

        expected_amount = "1"
        print("expected_amount", expected_amount)
        actual_amount = self.find_element(*self.ACTUAL_AMOUNT_TOP_NAV_MENU).text
        print("actual_amount", actual_amount)
        assert actual_amount == expected_amount, 'amount mismatching.'

    def verify_product_subtotal(self):
        original_product_price = self.find_element(*self.ORIGINAL_PRODUCT_PRICE).text
        # print('original_product_price', original_product_price)
        subtotal_price = self.find_element(*self.SUBTOTAL_PRICE).text
        # print('subtotal:', subtotal_price)
        original_product = self.find_element(*self.ORIGINAL_PRODUCT_NAME).text
        # print(original_product)
        expected_product = self.find_element(*self.EXPECTED_PRODUCT_NAME).text
        # print(expected_product)
        assert expected_product == original_product, f'{original_product} name and {expected_product} name not same.'
        assert subtotal_price == original_product_price, 'Both price are not same!'

    def verify_view_cart_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.VIEW_CART_BTN)).click()
        self.verify_url_contains_query('https://gettop.us/cart/')

    def verify_check_out_btn_clickable(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_OUT_BTN)).click()
        self.verify_url_contains_query('https://gettop.us/checkout/')

    def verify_remove_product(self):
        self.wait.until(EC.element_to_be_clickable(self.CROSS_SYMBOL_ICON)).click()
        print("icon is clickable.")
        self.wait.until(EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE))
        print('cart is empty.')
        sleep(4)
