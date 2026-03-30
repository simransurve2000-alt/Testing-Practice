from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

def test_secure_login():
    # 1. Setup
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # 2. Navigate to the Login Page
        driver.get("https://the-internet.herokuapp.com/login")
        
        # 3. Find elements and type
        # Locate by ID is the most reliable way!
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        
        # 4. Click the Login button (using CSS Selector)
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()
        
        # 5. Verification (Assert)
        time.sleep(2) # Brief pause to see the result
        success_message = driver.find_element(By.ID, "flash").text
        
        # Check if "You logged into a secure area!" is in the message
        assert "You logged into" in success_message
        print("Login Test Passed!")

    finally:
        # 6. Cleanup
        driver.quit()