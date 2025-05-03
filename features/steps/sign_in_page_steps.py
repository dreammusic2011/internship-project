from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.sign_in_page.open_main_page()
    sleep(2)

@when('Log in to the page')
def click_username(context):
    context.app.sign_in_page.type_email()
    context.app.sign_in_page.type_password()
    context.app.sign_in_page.click_sign_in_button()
    sleep(5)
