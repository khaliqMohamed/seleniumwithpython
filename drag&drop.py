from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source=driver.find_element(By.XPATH,'//*[@id="box4"]')
target=driver.find_element(By.XPATH,'//*[@id="box107"]')

actions=ActionChains(driver)
time.sleep(3)
actions.drag_and_drop(source,target).perform()
time.sleep(3)