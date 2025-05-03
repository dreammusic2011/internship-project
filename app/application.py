from pages.base_page import Page
# from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.side_nav_page import SideNavPage
from pages.settings_page import SettingsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(driver)
        # self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.base_page = Page(driver)
        self.side_nav_page = SideNavPage(driver)
        self.settings_page = SettingsPage(driver)