from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo/on-dom-element.html")

button=driver.find_element(By.XPATH,'//*[@id="the-node"]/li[1]/span')
time.sleep(3)

action=ActionChains(driver)
time.sleep(3)
action.context_click(button).perform()
time.sleep(3)