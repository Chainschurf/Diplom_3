from selenium.webdriver.common.by import By


class CreatingOrderPageLocators:

    CLOSE_MODAL_BUTTON = By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]"
    INGREDIENT_COUNTER = By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter_counter')]"
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    ORDER_CONFIRMATION_MODAL = By.XPATH, "//p[contains(text(), 'идентификатор заказа')]//ancestor::div[contains(@class, 'modal__container')]//h2[starts-with(text(), '14')]"
