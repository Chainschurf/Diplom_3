import allure


@allure.suite("Password Restore Page Tests")
@allure.title("Test Password Restore Page")
class TestPasswordRestorePage:

    @allure.title("Navigate to Password Restore Page")
    @allure.description("Checks navigation to the password restore page on 'Restore Password' button click.")
    def test_switching_to_password_restore_page(self, password_restore_page):
        password_restore_page.entering_login_page()
        password_restore_page.load_login_page()
        password_restore_page.clicking_restore_password()

        restore_page = password_restore_page.get_restore_page()

        assert restore_page.is_displayed(), "Failed to navigate to the password restore page."

    @allure.title("Enter Email and Click 'Restore'")
    @allure.description("Verifies that email can be entered, and 'Restore' button is functional.")
    def test_restore_email_click(self, password_restore_page):
        password_restore_page.entering_login_page()
        password_restore_page.load_login_page()
        password_restore_page.clicking_restore_password()
        password_restore_page.enter_email()
        password_restore_page.click_restore_button()

        code_field = password_restore_page.get_enter_code_field()

        assert code_field.is_displayed(), "The code entry field did not appear after clicking the 'Restore' button."

    @allure.title("Activate Password Field with Show/Hide Password Button")
    @allure.description("Checks that the show/hide password button activates and highlights the password field.")
    def test_password_field_active(self, password_restore_page):
        password_restore_page.entering_login_page()
        password_restore_page.load_login_page()
        password_restore_page.clicking_restore_password()
        password_restore_page.enter_email()
        password_restore_page.click_restore_button()
        password_restore_page.click_show_password_icon()

        active_field = password_restore_page.password_field_active()

        assert active_field, "The password field did not become active after clicking the show/hide password button."
