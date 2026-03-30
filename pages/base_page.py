from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """Finds an element using explicit wait to avoid flakiness."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Waits for an element and clicks it."""
        self.find(locator).click()

    def type(self, locator, text):
        """Waits for an element and sends keys."""
        self.find(locator).send_keys(text)
