from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")


driver.get("https://testautomationpractice.blogspot.com/")


driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)
driver.switch_to.alert.accept()
driver.quit()