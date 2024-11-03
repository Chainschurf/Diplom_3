import allure
from data import Links


@allure.suite("Main Page Tests")
@allure.title("Test Main Page")
class TestMainPage:

    @allure.title("Clicking on 'Constructor' button")
    @allure.description("Verifying navigation to the constructor page by clicking the 'Constructor' button.")
    def test_click_constructor(self, main_page, header_page):
        main_page.load_the_main_page()
        header_page.click_order_feed()
        header_page.click_constructor()

        current_url = main_page.driver.current_url

        assert current_url == Links.URL, "Did not navigate to the Constructor page."

    @allure.title("Clicking on 'Order Feed' button")
    @allure.description("Verifying navigation to the order feed page by clicking the 'Order Feed' button.")
    def test_click_order_feed(self, header_page):
        header_page.click_order_feed()

        assert header_page.driver.current_url.endswith("/feed"), "Did not navigate to the Order Feed page."

    @allure.title("Opening ingredient details modal")
    @allure.description("Verifying the ingredient details modal appears upon clicking an ingredient.")
    def test_ingredient_details_modal(self, main_page):
        main_page.click_ingredient()

        modal = main_page.get_ingredient_details_modal()

        assert modal.is_displayed(), "Ingredient details modal did not appear."

    @allure.title("Closing the ingredient details modal")
    @allure.description("Verifying the ingredient details modal closes correctly.")
    def test_close_ingredient_modal(self, main_page):
        main_page.click_ingredient()
        main_page.close_ingredients_modal()

        modal_is_gone = main_page.is_ingredient_modal_invisible()

        assert modal_is_gone, "Ingredient details modal did not close properly."

    @allure.title("Adding ingredient to order by drag-and-drop")
    @allure.description("Verifying an ingredient can be added to the order by dragging it into the order area.")
    def test_add_ingredient_to_order(self, creating_order_page):
        creating_order_page.drag_ingredient_to_order()

        ingredient_in_order_count = creating_order_page.get_ingredient_counter()

        assert int(ingredient_in_order_count) > 0, "Ingredient was not added to the order after dragging."

    @allure.title("Placing an order for a logged-in user")
    @allure.description("Verifying a logged-in user can place an order and see the order confirmation modal.")
    def test_logged_in_user_can_place_order(self, creating_order_page, login_page, create_test_user):
        email, password, token = create_test_user
        login_page.logging_in(email, password)
        creating_order_page.drag_ingredient_to_order()
        creating_order_page.confirm_order()

        assert creating_order_page.is_order_confirmation_modal_visible(), "Order confirmation modal did not appear."
