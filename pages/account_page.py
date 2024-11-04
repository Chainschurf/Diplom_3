import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators


class AccountPage(BasePage):

    @allure.step("Retrieving the account page element")
    def get_account_page(self):
        element = self.find_element(AccountPageLocators.ACCOUNT_PAGE, 10)
        return element

    @allure.step("Clicking the history button on account page")
    def clicking_history_button(self):
        self.click_element(AccountPageLocators.ORDER_HISTORY_BUTTON, 20)

    @allure.step("Clicking the exit button on account page")
    def clicking_exit_button(self):
        self.click_element(AccountPageLocators.EXIT_BUTTON)

    @allure.step("Retrieving the login page element after exit")
    def get_login_page(self):
        element = self.find_element(LoginPageLocators.LOGIN_PAGE, 10)
        return element
