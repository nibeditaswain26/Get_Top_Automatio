from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.base_page import Page


class Header(Page):
    IPHONE_BTN = (By.ID, 'menu-item-469')
    IPHONE_DROP_DOWN = (By.CSS_SELECTOR, 'a[href="#"]')

    def hover_over_to_iphone(self, button_name):
        self.wait.until(EC.presence_of_element_located(self.IPHONE_DROP_DOWN), message=f'{button_name} not found.')
        btn_name = self.driver.find_element(*self.IPHONE_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_name)
        actions.perform()


