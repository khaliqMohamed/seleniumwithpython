from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get("https://www.amazon.in/")


mobiles=driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[3]")
accessories=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[6]/div/a[3]/span[1]")
samsung=driver.find_element(By.XPATH,"//*[@id='nav-flyout-aj:https://images-eu.ssl-images-amazon.com/images/G/31/img18/Electronics/Megamenu/megamenumar18f.json:subnav-sl-megamenu-2:0']/div[2]/div/div[3]/h3[1]/a")

actions=ActionChains(driver)

actions.move_to_element(mobiles).move_to_element(accessories).move_to_element(samsung).click().perform()

time.sleep(5)

driver.quit()