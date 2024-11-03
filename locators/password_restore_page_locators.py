from selenium.webdriver.common.by import By


class PasswordRestorePageLocators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']/parent::a"
    RESTORE_PASSWORD_BUTTON = By.XPATH, "//a[contains(@href, '/forgot-password')]"
    EMAIL_FIELD = By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default')]"
    SHOW_PASSWORD_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon input__icon-action')]"
    SHOW_PASSWORD_ACTIVE = By.XPATH, "//div[contains(@class, 'input_status_active')]"
    RESTORE_PASSWORD_TEXT = By.XPATH, "//h2[text()='Восстановление пароля']"
    RESTORE_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    ENTER_CODE_FIELD = By.XPATH, "//label[text()='Введите код из письма']"
