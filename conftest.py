import allure
import pytest
from selenium import webdriver
from data import Links
from pages.header_page import HeaderPage
from pages.password_restore_page import PasswordRestorePage
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.creating_order_page import CreatingOrderPage
from user_api import UserAPI


def browser_settings(browser_name):
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
#        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        return chrome_options
    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--window-size=1920,1080')
        return firefox_options
    else:
        raise ValueError("Unsupported browser: {}".format(browser_name))


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        metafunc.parametrize("browser", ["chrome", "firefox"], indirect=True)


@pytest.fixture
def browser(request):
    browser_name = request.param
    options = browser_settings(browser_name)
    with allure.step(f"Initializing {browser_name} browser"):
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError("Invalid browser value provided")
        driver.get(Links.URL)

        yield driver

        with allure.step(f"Closing {browser_name} browser"):
            driver.quit()


@pytest.fixture
def create_test_user():
    email = UserAPI.generate_random_email()
    password = UserAPI.generate_random_password()
    user_data = UserAPI.register_new_user(email, password)
    token = user_data["accessToken"]

    yield email, password, token

    clean_token = token.replace("Bearer ", "")
    UserAPI.delete_user(clean_token)


@pytest.fixture
def password_restore_page(browser):
    return PasswordRestorePage(browser)


@pytest.fixture
def account_page(browser):
    return AccountPage(browser)


@pytest.fixture
def main_page(browser):
    return MainPage(browser)


@pytest.fixture
def order_feed_page(browser):
    return OrderFeedPage(browser)


@pytest.fixture
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture
def creating_order_page(browser):
    return CreatingOrderPage(browser)


@pytest.fixture
def header_page(browser):
    return HeaderPage(browser)
