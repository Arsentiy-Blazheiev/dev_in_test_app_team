from .page import Page
from appium.webdriver.common.mobileby import MobileBy as By


class LoginPage(Page):
    LOGIN_FIELD = (By.ID, "login_field_id")
    PASSWORD_FIELD = (By.ID, "password_field_id")
    LOGIN_BUTTON = (By.ID, "login_button_id")

    def enter_username(self, username: str):
        login_field = self.find_element(*self.LOGIN_FIELD)
        login_field.send_keys(username)

    def enter_password(self, password: str):
        password_field = self.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)
