from selenium import  webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.implicitly_wait(5)
#driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.set_page_load_timeout(10)

#finding how many text boxes present in the web page
#All text feilds have same class - text_field

inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Anand")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Soraganvi")
driver.find_element(By.ID,"RESULT_TextField-3").send_keys("3333333333")
driver.find_element(By.ID,"RESULT_TextField-4").send_keys("Canada")
driver.find_element(By.ID,"RESULT_TextField-5").send_keys("Ottawa")

driver.find_element(By.ID,"RESULT_TextField-5").location_once_scrolled_into_view
driver.find_element(By.ID,"RESULT_TextField-6").send_keys("abcd@abcd.com")
status1=driver.find_element(By.XPATH,"//*[@id='RESULT_RadioButton-7_0']").is_selected()
status2=driver.find_element(By.XPATH,"//*[@id='RESULT_CheckBox-8_3']").is_selected()
print(status1,status2)
time.sleep(2)

driver.find_element(By.XPATH, "//label[contains(text(),'Female')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[contains(text(),'Wednesday')]").click()
time.sleep(2)

driver.find_element(By.ID, "RESULT_RadioButton-9").click()
dropdown = driver.find_element(By.XPATH, "//*[@id='RESULT_RadioButton-9']/option[4]").click()
driver.find_element(By.ID, "RESULT_RadioButton-9").click()
driver.find_element(By.CSS_SELECTOR, ".icon_calendar").click()
driver.find_element(By.LINK_TEXT, "19").click()
element = driver.find_element(By.LINK_TEXT, "Software Testing Tutorials")
element.location_once_scrolled_into_view
driver.find_element(By.ID, "RESULT_TextArea-12").click()
driver.find_element(By.ID, "RESULT_TextArea-12").send_keys("adads")
driver.find_element(By.ID, "FSsubmit").click()

print(driver.title)
print(driver.find_element_by_id("content").text)

