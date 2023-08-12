from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time

browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser.get("https://www.flipkart.com/")

browser.maximize_window()

time.sleep(3)
login_close_button=browser.find_element(By.XPATH,'//div[@tabindex=-1]/div/button').click()
browser.find_element(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys('shoes')
browser.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()


time.sleep(5)
browser.quit()

