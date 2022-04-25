from selenium.webdriver.common.by import By
from page.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(Page):

    def verify_product_page(self, product_page):
        self.verify_url_contains_query(product_page)
