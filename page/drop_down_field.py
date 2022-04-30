from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.base_page import Page


class DropDown(Page):
    iphone_12 = (By.ID, 'menu-item-484')
    case_protection = (By.ID, 'menu-item-485')
    ipad_mini = (By.ID, 'menu-item-388')
    macBook_pro_13_inch = (By. ID, 'menu-item-389')

    def click_on_drop_down_btn(self, product_name):

        product_btn = self.driver.find_element(*self.macBook_pro_13_inch)
        actions = ActionChains(self.driver)
        actions.move_to_element(product_btn)
        actions.click(product_btn)
        self.wait.until(EC.visibility_of_element_located(self.macBook_pro_13_inch), message=f'{product_name} is not found.')
        actions.perform()



