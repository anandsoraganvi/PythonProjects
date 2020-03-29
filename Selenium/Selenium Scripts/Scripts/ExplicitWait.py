
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.expedia.ca/")
driver.set_page_load_timeout(10)
driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)

driver.find_element(By.ID,"flight-origin-hp-flight").click()
time.sleep(2)

#driver.find_element(By.ID,"flight-origin-hp-flight").clear()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)

driver.find_element(By.ID,"flight-destination-hp-flight").clear()
time.sleep(5)
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
time.sleep(5)


driver.find_element(By.ID,"flight-returning-hp-flight").clear()
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("22/07/2019")
time.sleep(2)

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("19/07/2019")
time.sleep(2)


driver.find_element(By.XPATH,"//*[@id='flight-departing-wrapper-hp-flight']/div/div/div[1]/button").click()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='traveler-selector-hp-flight']/div/ul/li/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='traveler-selector-hp-flight']/div/ul/li/div/footer/div/div[2]/button").click()
time.sleep(2)



driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


wait=WebDriverWait(driver,15)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stopFilter_stops-0']")))
element.click()
driver.close()

