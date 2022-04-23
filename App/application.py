from page.main_page import MainPage
from page.header import Header
from page.drop_down_field import DropDown
from page.product_page  import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.drop_down_field = DropDown(self.driver)
        self.product_page = ProductPage(self.driver)