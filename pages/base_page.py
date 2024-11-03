import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        else:
            pytest.fail(f"Failed to click on element with locator {locator}.")

    def get_text_from_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text

    def wait_for_element_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            print(f"Element with {locator} did not become visible after {timeout} seconds.")
            return None

    def wait_for_element_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            pytest.fail(f"Element with locator {locator} did not become invisible within {timeout} seconds.")

    def is_element_invisible(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False

    def is_element_visible(self, locator, timeout=10):

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
