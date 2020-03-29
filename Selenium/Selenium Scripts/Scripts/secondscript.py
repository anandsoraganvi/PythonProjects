from selenium import webdriver

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")


class Facebook():

    def setup(self):
        driver.maximize_window()
        driver.get("http://facebook.com")

    def waiti(self):
        driver.set_page_load_timeout(20)
        driver.find_element_by_id("email").send_keys("ana.soraganvi@gmail.com")
        driver.find_element_by_id("pass").send_keys("Welcome2ottawa")
        driver.find_element_by_id("loginbutton").click()
        driver.implicitly_wait(10)

    def takescreenshot(self):
        driver.get_screenshot_as_file(".\\Screenshots\\facebook.png")

    def basic(self):
        print(driver.title)
        print(driver.current_url)

    def quitd(self):
        driver.close()
        driver.quit()


F = Facebook()
F.setup()
F.waiti()
F.basic()
F.takescreenshot()
print("Passed")
