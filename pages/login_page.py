import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Clicking on 'Account' button to navigate based on user state")
    def clicking_account_button(self):
        self.click_element(LoginPageLocators.ACCOUNT_BUTTON, 15)

    @allure.step("Logging in with email: {email} and password")
    def logging_in(self, email, password):
        self.clicking_account_button()
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email)
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
        self.click_element(LoginPageLocators.ENTER_BUTTON)
