import allure
from data import Links


@allure.suite("Account Page Tests")
@allure.title("Test Account Page")
class TestAccountPage:

    @allure.title("Verify navigation to 'Личный кабинет'")
    @allure.description("Testing that clicking on 'Личный кабинет' navigates the user to the account page.")
    def test_entering_account_page(self, account_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        login_page.clicking_account_button()

        personal_account = account_page.get_account_page()

        assert personal_account.is_displayed()

    @allure.title("Verify navigation to 'История заказов' section")
    @allure.description("Testing that clicking on 'История заказов' navigates the user to the order history section.")
    def test_entering_order_history_page(self, account_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        login_page.clicking_account_button()
        account_page.clicking_history_button()

        expected_url = Links.ORDER_PAGE_URL

        assert account_page.driver.current_url == expected_url, f"Expected URL {expected_url} but got {account_page.driver.current_url}"

    @allure.title("Verify user can log out of their account")
    @allure.description("Testing that clicking the 'Выход' button logs the user out.")
    def test_exit_account(self, account_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        login_page.clicking_account_button()
        account_page.clicking_exit_button()

        login_page_check = account_page.get_login_page()

        assert login_page_check.is_displayed()
