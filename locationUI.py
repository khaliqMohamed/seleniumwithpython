from selenium import webdriver
#from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
import time

web_browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
web_browser.get("https://www.instagram.com/")

web_browser.maximize_window()
time.sleep(10)

frgtpwd=web_browser.find_element(By.XPATH,'//*[@id="loginForm"]/a').click()

time.sleep(10)

web_browser.get_screenshot_as_file("img4.png")

web_browser.quit()