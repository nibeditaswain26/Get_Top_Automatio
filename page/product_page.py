from selenium.webdriver.common.by import By
from page.base_page import Page


class ProductPage(Page):

    def verify_product_page(self, product_page):
        self.verify_url_contains_query('https://gettop.us/product/iphone-12/')
