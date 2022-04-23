from selenium.webdriver.common.by import By
from page.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):

    def verify_product_page(self, product_page):
        self.wait.until(EC.url_contains('https://gettop.us/product/iphone-12/'), message=f'{product_page} page is not found.')
