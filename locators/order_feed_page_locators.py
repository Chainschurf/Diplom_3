from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    ORDER_ITEM = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]"
    ORDER_DETAILS_MODAL = By.XPATH, "//div[contains(@class, 'Modal_orderBox')]"
    ORDER_LIST = By.XPATH, "//div[contains(@class, 'OrderHistory_orderHistory')]"
    TOTAL_COMPLETED_COUNTER = By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p"
    TODAY_COMPLETED_COUNTER = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p"
    IN_PROGRESS_SECTION = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    OLD_READY_TEXT = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[text()='Все текущие заказы готовы!']"


