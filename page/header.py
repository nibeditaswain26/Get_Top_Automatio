from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.base_page import Page


class Header(Page):
    IPHONE_BTN = (By.ID, 'menu-item-469')
    IPHONE_DROP_DOWN = (By.CSS_SELECTOR, 'a[href="#"]')
    ACCESSORIES_BTN = (By.ID, 'menu-item-472')
    ACCESSORIES_DROP_DOWN = (By.CSS_SELECTOR, 'a[href="https://gettop.us/product-category/accessories/airpods/"]')
    IPAD_BTN = (By.ID, 'menu-item-470')
    IPAD_DROP_DOWN = (By.CSS_SELECTOR, '#menu-item-470 li')
    CART_ICON = (By.CSS_SELECTOR, '.cart-icon.image-icon')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'li.html.widget_shopping_cart')
    MAC_BTN = (By.ID, 'menu-item-468')
    MAC_DROPDOWN = (By.CSS_SELECTOR, '#menu-item-468 li')


    def hover_over_to_header_btn(self, button_name):
        btn_name = self.driver.find_element(*self.MAC_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_name)
        self.wait.until(EC.presence_of_element_located(self.MAC_DROPDOWN), message=f'{button_name} not found.')
        actions.perform()

    def click_on_cart_icon(self):
        self.find_element(*self.CART_ICON).click()

    def hover_to_cart_icon(self):
        cart_icon = self.driver.find_element(*self.CART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_icon)
        actions.perform()

    def verify_message(self):
        self.wait.until(EC.presence_of_element_located(self.EMPTY_CART_MESSAGE), message='Empty message is not popping up.')



