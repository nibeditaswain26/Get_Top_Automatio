from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page.base_page import Page

IPHONE_12 = (By.ID, 'menu-item-484')


class DropDown(Page):
    def click_on_iphone_12(self):
        iphone_12_btn = self.driver.find_element(*IPHONE_12)
        actions = ActionChains(self.driver)
        actions.move_to_element(iphone_12_btn)
        actions.click(iphone_12_btn)
        actions.perform()

