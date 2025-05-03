from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):

    SETTINGS_OPTIONS = (By.CSS_SELECTOR, "[class*='page-setting-block']")
    CONNECT_COMPANY = (By.CSS_SELECTOR, "[class='get-free-period menu']")


    def verify_options_present(self, expected_count):
        self.wait_until_visible(*self.SETTINGS_OPTIONS)
        links = self.find_elements(*self.SETTINGS_OPTIONS)
        assert len(links) == int(expected_count), f"Expected {expected_count} links, got {len(links)}"


    def verify_connect_company_btn(self):
        self.wait_until_visible(*self.CONNECT_COMPANY)
        elements = self.find_elements(*self.CONNECT_COMPANY)
        assert elements, "Connect Company button not found"