from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.creating_order_page_locators import CreatingOrderPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Loading the main page")
    def load_the_main_page(self):
        self.wait_for_element_visible(HeaderPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Clicking on an ingredient to view details")
    def click_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_BULKA)

    @allure.step("Getting ingredient details modal")
    def get_ingredient_details_modal(self):
        return self.wait_for_element_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Closing the ingredient details modal")
    def close_ingredients_modal(self):
        self.click_element(CreatingOrderPageLocators.CLOSE_MODAL_BUTTON)
        self.wait_for_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

    @allure.step("Checking if the ingredient modal is invisible")
    def is_ingredient_modal_invisible(self):
        return self.is_element_invisible(MainPageLocators.INGREDIENT_DETAILS_MODAL)

