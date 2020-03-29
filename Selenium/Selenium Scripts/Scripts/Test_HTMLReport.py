from selenium import webdriver
import unittest
from HtmlTestRunner import HTMLTestRunner
import time
#from filecmp import f


class TestOrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        driver=webdriver.Chrome("C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
        driver.maximize_window()
        print("Browser Started\n")

    def test_HomePageTitle(self):
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
        time.sleep(5)
        self.assertEqual("OrangeHRM",driver.title,"WebPage title is not matching")
        print("Title is matched")

    def test_Login(self):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", driver.title, "WebPage title is not matching")
        print("Login Successfull")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        print("Browser Closed and Test Completed\n")

if __name__=='main':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite(loader.loadTestsFromTestCase(TestOrangeHRMTest))
    outfile = ('Reports.html', 'w')
    runner = HTMLTestRunner(stream=outfile,
                            verbosity=2,
                            title='LinkedIn Report',
                            description='This is a demo report')
    runner.run(suite)
    #HTMLTestRunner.main().main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users/anaso/PycharmProjects/Selenium/Selenium Scripts/HTMLReports'))

