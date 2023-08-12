from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")


driver.get("https://testautomationpractice.blogspot.com/")

element=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)
time.sleep(5)
actions.double_click(element).perform()
