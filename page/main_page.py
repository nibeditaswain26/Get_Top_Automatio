from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from page.base_page import Page
from time import sleep


class MainPage(Page):
    RIGHT_ARROW_ON_BANNER = (By.XPATH, '//div[@class="slider slider-nav-circle '
                                       'slider-nav-large slider-nav-light slider-style-normal '
                                       'flickity-enabled is-draggable"]'
                                       '//button[@aria-label="Next"]//*[name()="svg"]')
    LEFT_ARROW_ON_BANNER = (By.XPATH, '//div[@class="slider slider-nav-circle '
                                       'slider-nav-large slider-nav-light slider-style-normal '
                                       'flickity-enabled is-draggable"]'
                                       '//button[@aria-label="Previous"]//*[name()="svg"]')
    TOP_BANNERS = (By.CSS_SELECTOR, '.fill.banner-link')
    BOTTOM_DOTS = (By.CSS_SELECTOR, '.flickity-page-dots li')
    MAC_BOOK_BANNER = (By.CSS_SELECTOR, 'div[class="banner-layers container"] a[href="/product-category/macbook/"]')
    IPAD_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/ipad/"] div')

    def open_get_top(self):
        self.open_page()

    def left_right_arrow_banner(self):
        self.find_element(*self.RIGHT_ARROW_ON_BANNER).click()
        sleep(2)
        print("Right arrow is clickable")

        self.find_element(*self.LEFT_ARROW_ON_BANNER).click()
        print("Left arrow is clickable")
        sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.TOP_BANNERS))
        print('Top banners are visible.')

    def click_bottom_dots(self):
        botm_dots = self.find_elements(*self.BOTTOM_DOTS)
        for dot in botm_dots:
            dot.click()
            sleep(2)
            self.wait.until(EC.presence_of_element_located(self.TOP_BANNERS))

        print('dots are clickable.')
        print('top banner are visible.')
        # self.driver.refresh()

    def product_banners_clickable(self):
        element = self.find_element(*self.MAC_BOOK_BANNER)
        self.driver.execute_script("arguments[0].click();", element)
        self.verify_url_contains_query('/product-category/macbook/')
        self.open_get_top()
        element = self.find_element(*self.IPAD_BANNER)
        self.driver.execute_script("arguments[0].click();", element)
        self.verify_url_contains_query('/product-category/ipad/')
        print('banners are clickable and taking to correct page.')



