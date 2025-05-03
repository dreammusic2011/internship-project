from behave import given, when, then

@when('Verify {expected_count} setting options are present')
def verify_options_settings(context, expected_count):
    context.app.settings_page.verify_options_present(expected_count)

@then('Verify button')
def verify_button_pressed(context):
    context.app.settings_page.verify_connect_company_btn()