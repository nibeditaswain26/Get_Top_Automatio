from selenium.webdriver.common.by import By
from page.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):
    ipad_mini_left_right_arrow = (By.CSS_SELECTOR, 'ul[class="next-prev-thumbs is-small nav-right text-right"] li')
    IPAD_DROP_DOWN = (By.CSS_SELECTOR, '#menu-item-470 li')
    USER_RATTING = (By.CSS_SELECTOR, '.woocommerce-product-rating')

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
