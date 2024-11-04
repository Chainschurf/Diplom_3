import allure
from pages.base_page import BasePage
from locators.password_restore_page_locators import PasswordRestorePageLocators
from locators.login_page_locators import LoginPageLocators
from data import Links


class PasswordRestorePage(BasePage):

    @allure.step("Entering the login page")
    def entering_login_page(self):
        self.click_element(PasswordRestorePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Waiting for login page to load")
    def load_login_page(self):
        self.wait_for_element_visible(LoginPageLocators.LOGIN_PAGE)

    @allure.step("Clicking on 'Restore Password' button")
    def clicking_restore_password(self):
        self.click_element(PasswordRestorePageLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Waiting for password restore page to load")
    def loading_restore_page(self):
        self.wait_for_element_visible(PasswordRestorePageLocators.RESTORE_PASSWORD_TEXT)

    @allure.step("Retrieving the password restore page element")
    def get_restore_page(self):
        element = self.find_element(PasswordRestorePageLocators.RESTORE_PASSWORD_TEXT, 10)
        return element

    @allure.step("Entering email for password restore")
    def enter_email(self):
        self.enter_text(PasswordRestorePageLocators.EMAIL_FIELD, Links.DEFAULT_TEST_EMAIL)

    @allure.step("Clicking the 'Restore' button")
    def click_restore_button(self):
        self.click_element(PasswordRestorePageLocators.RESTORE_BUTTON)

    @allure.step("Retrieving 'Enter Code' field element")
    def get_enter_code_field(self):
        element = self.find_element(PasswordRestorePageLocators.ENTER_CODE_FIELD, 10)
        return element

    @allure.step("Clicking the show password icon")
    def click_show_password_icon(self):
        self.click_element(PasswordRestorePageLocators.SHOW_PASSWORD_BUTTON, 10)

    @allure.step("Checking if the password field is active")
    def password_field_active(self):
        element = self.find_element(PasswordRestorePageLocators.SHOW_PASSWORD_ACTIVE, 10)
        return element
