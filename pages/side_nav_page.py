from selenium.webdriver.common.by import By

from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class SideNavPage(Page):

    OPEN_SETTINGS = (By.CSS_SELECTOR, "[href='/settings']")
    MENU_BLOCK = (By.CSS_SELECTOR, "[class='menu-block']")
    OPEN_MOBILE = (By.CSS_SELECTOR, "[class*='settings-link']")

    def open_settings(self):
        # elements = self.find_elements(*SideNavPage.OPEN_SETTINGS)
        # elements[2].click()
        self.wait_until_clickable_click(*self.OPEN_MOBILE)

    def scroll_to_element(self, locator):
        self.scroll_click(*self.OPEN_SETTINGS)