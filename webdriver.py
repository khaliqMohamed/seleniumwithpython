from selenium import webdriver
import time 

browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser.get("https://www.google.co.in/")

time.sleep(3)

browser.get_screenshot_as_file("google_ss.png")

browser.get("https://www.instagram.com/")

time.sleep(3)

browser.get_screenshot_as_file("insta_ss.png")

browser.back()

time.sleep(3)

browser.forward()

time.sleep(2)
browser.quit()