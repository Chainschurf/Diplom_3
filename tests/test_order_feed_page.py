import allure


@allure.suite("Order Feed Page Tests")
@allure.title("Test Order Feed Page")
class TestOrderFeedPage:

    @allure.title("Viewing order details by clicking on an order")
    @allure.description("Verifying the order details modal appears when clicking on an order in the feed.")
    def test_click_order_and_view_details(
            self, creating_order_page, order_feed_page, login_page, create_test_user, header_page):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        creating_order_page.create_order()
        header_page.click_order_feed()
        order_feed_page.click_on_order()

        modal = order_feed_page.get_order_details_modal()

        assert modal.is_displayed(), "Order details modal did not open."

    @allure.title("Verifying user orders displayed in the Order Feed")
    @allure.description("Checking that orders placed by the user appear in the Order Feed section.")
    def test_user_orders_displayed_in_order_feed(
            self, creating_order_page, header_page, order_feed_page, account_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        creating_order_page.create_order()
        login_page.clicking_account_button()
        account_page.clicking_history_button()
        order_history_orders = order_feed_page.get_order_identifiers()
        header_page.click_order_feed()

        order_feed_orders = order_feed_page.get_in_progress_orders()

        for order in order_history_orders:
            assert order in order_feed_orders, f"Order {order} from history is not displayed in the order feed."

    @allure.title("Increasing total completed orders counter")
    @allure.description("Verifying the total completed orders counter increments after placing an order.")
    def test_total_completed_counter_increases(
            self, header_page, creating_order_page, order_feed_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        header_page.click_order_feed()
        initial_completed_count = order_feed_page.get_total_completed_count()
        header_page.click_constructor()
        creating_order_page.create_order()
        header_page.click_order_feed()

        final_completed_count = order_feed_page.get_total_completed_count()

        assert final_completed_count > initial_completed_count, "Total completed orders counter did not increase."

    @allure.title("Increasing today's completed orders counter")
    @allure.description("Verifying the counter for today's completed orders increments after placing an order.")
    def test_today_completed_counter_increases(
            self, header_page, creating_order_page, order_feed_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        header_page.click_order_feed()
        initial_today_count = order_feed_page.get_today_completed_count()
        header_page.click_constructor()
        creating_order_page.create_order()
        header_page.click_order_feed()

        final_today_count = order_feed_page.get_today_completed_count()

        assert final_today_count > initial_today_count, "Today's completed orders counter did not increase."

    @allure.title("Verifying order appears in the 'In Progress' section")
    @allure.description("Checking if the newly placed order shows up in the 'In Progress' section of the Order Feed.")
    def test_order_appears_in_progress(
            self, header_page, creating_order_page, order_feed_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        creating_order_page.drag_ingredient_to_order()
        creating_order_page.confirm_order()
        new_order_number = order_feed_page.get_order_number_from_confirmation_modal()
        creating_order_page.close_modal()
        header_page.click_order_feed()

        in_progress_orders = order_feed_page.get_in_progress_orders()

        assert new_order_number in in_progress_orders, f"Order {new_order_number} did not appear in the 'In Progress' section."
