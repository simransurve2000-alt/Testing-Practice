import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        # This setup runs before every test
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_successful_login(self):
        login = LoginPage(self.driver)
        # Using the clean methods we created in our Page Objects
        login.login_to_app("Admin", "admin123")
        
        # Assertion: If the URL contains 'dashboard', the test passes!
        self.assertIn("dashboard", self.driver.current_url.lower())

    def tearDown(self):
        # This closes the browser after the test is done
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
