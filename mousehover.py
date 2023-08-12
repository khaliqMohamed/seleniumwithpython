from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get("https://www.ajio.com/")

mens=driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[1]/ul/li[1]/a")
categories=driver.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[3]/div[1]/ul/li[1]/div[1]/ul/li[1]/a")
collections=driver.find_element(By.XPATH,"//*[@id='third']/div[1]/a/span")



actions=ActionChains(driver)

actions.move_to_element(mens).move_to_element(categories).move_to_element(collections).click().perform()

time.sleep(5)

driver.quit()