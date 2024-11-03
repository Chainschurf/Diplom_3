import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Clicking on 'Order Feed' button")
    def click_order_feed(self):
        self.click_element(HeaderPageLocators.ORDER_FEED_BUTTON, 10)

    @allure.step("Clicking on 'Constructor' button")
    def click_constructor(self):
        self.click_element(HeaderPageLocators.CONSTRUCTOR_BUTTON, 10)