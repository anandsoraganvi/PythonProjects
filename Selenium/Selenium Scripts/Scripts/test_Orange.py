from selenium import webdriver
import pytest
#import time

class TestOrangeHRMTest():

    @pytest.fixture()
    def setup(self):
        global driver
        self.driver=webdriver.Chrome("C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        self.driver.maximize_window()
        print("Browser Started\n")
        yield
        self.driver.close()


    def test_HomePageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        #time.sleep(2)
        assert self.driver.title=="OrangeHRM"
        print("Title is matched")

    def test_Login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title=="OrangeHRM"
        print("Login Successfull")





