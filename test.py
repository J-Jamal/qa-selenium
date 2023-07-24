import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_success_login(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(5)
        browser.find_element(By.ID,"user-name").send_keys("standard_user") 
        browser.find_element(By.ID,"password").send_keys("secret_sauce") 
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click()
        time.sleep(5)
        response_message = browser.find_element(
            By.CLASS_NAME,"inventory_item_name").text
        self.assertEqual(response_message, 'Sauce Labs Backpack')

    def test_failed_login(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(5)
        browser.find_element(By.ID,"user-name").send_keys("test") 
        browser.find_element(By.ID,"password").send_keys("test") 
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click()
        time.sleep(5)
        response_message = browser.find_element(
            By.ID,"login_button_container").text
        self.assertIn('Username and password do not match any user in this service', response_message)

    def test_failed_login_empty(self):
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        time.sleep(5)
        browser.find_element(By.ID,"user-name").send_keys("") 
        browser.find_element(By.ID,"password").send_keys("") 
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click()
        time.sleep(5)
        response_message = browser.find_element(
            By.ID,"login_button_container").text
        self.assertIn('Username is required', response_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()