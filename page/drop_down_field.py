from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.base_page import Page


class DropDown(Page):
    iphone_12 = (By.ID, 'menu-item-484')
    case_protection = (By.ID, 'menu-item-485')

    def click_on_drop_down_btn(self, product_name):

        iphone_12_btn = self.driver.find_element(*self.case_protection)
        actions = ActionChains(self.driver)
        actions.move_to_element(iphone_12_btn)
        actions.click(iphone_12_btn)
        self.wait.until(EC.visibility_of_element_located(self.case_protection), message=f'{product_name} is not found.')
        actions.perform()



