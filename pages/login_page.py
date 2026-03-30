from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # These are 'Locators'. If the website changes, you only fix them here!
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login_to_app(self, user, pwd):
        """This method performs the full login flow."""
        self.type(self.USERNAME_FIELD, user)
        self.type(self.PASSWORD_FIELD, pwd)
        self.click(self.LOGIN_BUTTON)
