from selenium.webdriver.common.by import By


class AccountPageLocators:

    ACCOUNT_PAGE = By.XPATH, "//a[contains(@href, '/account/profile')]"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[contains(@href, '/account/order-history')]"
    EXIT_BUTTON = By.XPATH, "//button[text()='Выход']"
