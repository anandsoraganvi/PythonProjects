from selenium import webdriver
import unittest
import HtmlTestRunner
import time

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        cls.driver=webdriver.Chrome("C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        print("Browser Started\n")

    def test_HomePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        time.sleep(2)
        self.assertEqual("OrangeHRM",self.driver.title,"WebPage title is not matching")
        print("Title is matched")

    def test_Login(self):
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "WebPage title is not matching")
        print("Login Successfull")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Browser Closed and Test Completed\n")




if __name__=='main':
    unittest.main()

