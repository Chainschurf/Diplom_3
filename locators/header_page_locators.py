from selenium.webdriver.common.by import By


class HeaderPageLocators:

    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']/parent::a"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']/parent::a"