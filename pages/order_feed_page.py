import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.creating_order_page_locators import CreatingOrderPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Clicking on an order in the order feed")
    def click_on_order(self):
        self.click_element(OrderFeedPageLocators.ORDER_ITEM)

    @allure.step("Retrieving order identifiers from the order feed")
    def get_order_identifiers(self):
        orders = self.driver.find_elements(*OrderFeedPageLocators.ORDER_LIST)
        return [order.text for order in orders if order.text]

    @allure.step("Getting the order details modal visibility")
    def get_order_details_modal(self):
        return self.wait_for_element_visible(OrderFeedPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Retrieving the total completed orders count")
    def get_total_completed_count(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_COMPLETED_COUNTER))

    @allure.step("Retrieving today's completed orders count")
    def get_today_completed_count(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER))

    @allure.step("Getting the order number from the confirmation modal")
    def get_order_number_from_confirmation_modal(self):
        order_number_element = self.find_element(CreatingOrderPageLocators.ORDER_CONFIRMATION_MODAL, 20)
        order_number_text = order_number_element.text.strip()

        return order_number_text

    @allure.step("Retrieving orders currently in progress")
    def get_in_progress_orders(self):
        if self.is_element_visible(OrderFeedPageLocators.OLD_READY_TEXT):
            self.wait_for_element_invisible(OrderFeedPageLocators.OLD_READY_TEXT, 15)
        orders_in_progress_elements = self.find_elements(OrderFeedPageLocators.IN_PROGRESS_SECTION)

        return [order.text.strip().lstrip('0') for order in orders_in_progress_elements]
