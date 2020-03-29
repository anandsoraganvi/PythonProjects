from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/anaso/PycharmProjects/Selenium/Selenium Scripts/Drivers/chromedriver.exe")
driver.implicitly_wait(5)
#driver.maximize_window()

driver.get("http://gmail.com")
driver.implicitly_wait(5)

driver.find_element_by_id("identifierId").send_keys("ana.soraganvi")
driver.implicitly_wait(5)
driver.find_element_by_id("identifierNext").click()




links=driver.find_elements_by_tag_name("a")
print("Number of links present on the page : ",len(links))

k=1
for i in links:
    print("Link #{:2}".format(k)," ",i.text)
    k+=1

#clicking on the links
#Way 1 : by using complete link text
#driver.find_element(By.LINK_TEXT,"REGISTER").click()
#Way 2 : by using partial link text
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()

