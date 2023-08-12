from selenium import webdriver
import time

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get("https://marlowpillow.com/?al_pg_id=9b3b6e5d-5335-4566-a83e-17f3529f1eef")

time.sleep(6)
driver.switch_to.alert.dismiss()

driver.quit()