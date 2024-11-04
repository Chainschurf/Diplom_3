from selenium.webdriver.common.by import By


class MainPageLocators:

    INGREDIENT_BULKA = By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]"
    ORDER_AREA = By.XPATH, "//div[contains(@class, 'constructor-element constructor-element_pos_top')]"
    INGREDIENT_DETAILS_MODAL = By.XPATH, "//h2[text()='Детали ингредиента']"
