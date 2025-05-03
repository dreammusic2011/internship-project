from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):

    SIGN_IN_TXT = (By.CSS_SELECTOR, "[class='form-header']")
    T_AND_C = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")
    SIGN_IN_TEXT = (By.ID, 'username')
    CLICK_EMAIL = (By.ID, 'email-2')
    CLICK_PASSWORD = (By.NAME, "Password")
    CLICK_SIGN_IN_BTN = (By.CSS_SELECTOR, "[class*='login-button']")


    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def verify_sign_in_text(self, expected_text):
        actual_text = self.find_element(*self.SIGN_IN_TXT).text
        assert expected_text in actual_text, f"Error. expected {expected_text} but got {actual_text}"

    def open_terms_page(self):
        self.click(*self.T_AND_C)

    def type_email(self):
        self.wait_until_clickable(*self.CLICK_EMAIL)
        self.input_text("dereklwestjr@gmail.com", *self.CLICK_EMAIL)


    def type_password(self):
        self.input_text("hebby0-giktap-ciKbad", *self.CLICK_PASSWORD)


    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions')

    def click_sign_in_button(self):
        self.click(*self.CLICK_SIGN_IN_BTN)