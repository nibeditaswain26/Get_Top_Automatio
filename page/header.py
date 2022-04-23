from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page.base_page import Page


IPHONE_BTN = (By.ID, 'menu-item-469')


class Header(Page):
    def hover_over_to_iphone_btn(self, btn_name):
        btn_name = self.driver.find_element(*IPHONE_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_name)
        actions.perform()
