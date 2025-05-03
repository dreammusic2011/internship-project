from behave import given, when, then



@when('Click on the settings option')
def open_settings(context):
    context.app.side_nav_page.open_settings()
