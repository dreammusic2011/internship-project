from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.chrome.options import Options as ChromeOptions

def browser_init(context):
    """
    :param context: Behave context
    """

    # Mobile

    # mobile_emulation = {
    #     "deviceName": "Pixel 2"  # You can also try "iPhone SE", "Galaxy S5", etc.
    # }
    #
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    bs_user = 'derekwest_yxqozL'
    bs_key = 'VqiVvX6PiPPQD4rnfnyN'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    bs_user = 'derekwest_yxqozL'
    bs_key = 'VqiVvX6PiPPQD4rnfnyN'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = ChromeOptions()


    bstack_options = {
        "deviceName": "Samsung Galaxy S22",
        "osVersion": "12.0",
        "realMobile": "true",
        "projectName": "Mobile Web Testing",
        "buildName": "Build 1",
        "sessionName": "Behave Test"
    }


    options.set_capability('bstack:options', bstack_options)
    options.set_capability('browserName', 'Chrome')  # Required for mobile web

    context.driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

    # Browserstack



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
def before_step(context, step):
    print('\nStarted step: ', step)
def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
def after_scenario(context, feature):
    context.driver.quit()