from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_experimental_option("prefs", {"download.default_directory": "C:\D"})
driver = webdriver.Chrome(
    executable_path="C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe",
    chrome_options=option)
driver.maximize_window()

# Site 1
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.set_page_load_timeout(4)

driver.find_element_by_xpath("/html/body/section/div[1]/div/div/h2").location_once_scrolled_into_view
driver.find_element_by_id("textbox").send_keys("Anand")
time.sleep(2)
driver.find_element_by_id("createTxt").click()
time.sleep(2)
driver.find_element_by_id("link-to-download").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div[3]/div[1]").location_once_scrolled_into_view
driver.find_element_by_id("pdfbox").send_keys("Anand Soraganvi")
time.sleep(2)
driver.find_element_by_id("createPdf").click()
time.sleep(2)
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(2)
