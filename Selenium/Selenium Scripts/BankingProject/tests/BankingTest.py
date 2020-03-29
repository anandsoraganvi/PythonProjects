from selenium import webdriver
import time
import unittest



class banking_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome("C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        time.sleep(2)
        cls.driver.maximize_window()

    def testBanking(self):
        driver=self.driver
        driver.get("https://portal.nationet.com/nationwide/current_account/applyredirect.asp?app=flexdirectnew")
        time.sleep(10)
        #driver.find_element_by_xpath("//*[@id='useOfInfoOverlay']/span[2]").location_once_scrolled_into_view()
        driver.find_element_by_xpath("//*[@id='useOfInfoOverlay']/span[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/footer/div/div/a").click()




    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Passed")
