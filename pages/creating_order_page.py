import allure
from selenium.webdriver import ActionChains
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.creating_order_page_locators import CreatingOrderPageLocators


class CreatingOrderPage(BasePage):

    @allure.step("Dragging ingredient to the order area")
    def drag_ingredient_to_order(self):
        ingredient = self.find_element(MainPageLocators.INGREDIENT_BULKA)
        order_area = self.find_element(MainPageLocators.ORDER_AREA)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, order_area).perform()

    @allure.step("Getting the ingredient counter in the order area")
    def get_ingredient_counter(self):
        return self.get_text_from_element(CreatingOrderPageLocators.INGREDIENT_COUNTER)

    @allure.step("Confirming the order")
    def confirm_order(self):
        self.click_element(CreatingOrderPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Checking if the order confirmation modal is visible")
    def is_order_confirmation_modal_visible(self):
        return self.wait_for_element_visible(CreatingOrderPageLocators.ORDER_CONFIRMATION_MODAL)

    @allure.step("Closing the order confirmation modal")
    def close_modal(self):
        self.wait_for_element_visible(CreatingOrderPageLocators.ORDER_CONFIRMATION_MODAL, 15)
        self.click_element(CreatingOrderPageLocators.CLOSE_MODAL_BUTTON, 15)
        self.wait_for_element_invisible(CreatingOrderPageLocators.ORDER_CONFIRMATION_MODAL, 15)

    @allure.step("Creating an order by dragging ingredient and confirming")
    def create_order(self):
        self.drag_ingredient_to_order()
        self.confirm_order()
        self.close_modal()
