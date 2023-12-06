# from appium.webdriver.common.by import By
# import appium.webdriver.common.by
from appium.webdriver.common.mobileby import MobileBy as By
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Page:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, by: By, value: str):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with {by}={value} not found within {self.timeout} seconds")

        # raise NotImplementedError

    def click_element(self, by: By, value: str):
        element = self.find_element(by, value)
        element.click()
        # raise NotImplementedError
