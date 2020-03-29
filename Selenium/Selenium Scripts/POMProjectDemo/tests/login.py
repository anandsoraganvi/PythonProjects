from selenium import  webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMProjectDemo.pages.LoginPage import LoginPage
from POMProjectDemo.pages.HomePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        time.sleep(1)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        time.sleep(2)

        loginpage=LoginPage(driver)
        loginpage.enter_username("Admin")
        loginpage.enter_password("admin123")
        loginpage.click_loginbutton()

        time.sleep(2)
        homepage=HomePage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test passed")


if __name__=="main":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/anaso/PycharmProjects/Selenium"))