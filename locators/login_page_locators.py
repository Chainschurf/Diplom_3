from selenium.webdriver.common.by import By


class LoginPageLocators:

    LOGIN_PAGE = By.XPATH, "//h2[text()='Вход']"
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/parent::div/input"
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']"
    ENTER_BUTTON = By.XPATH, "//button[text()='Войти']"
    ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']/parent::a"
