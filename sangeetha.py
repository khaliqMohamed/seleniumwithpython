from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as waitE

#open chrome browser
web_driver=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

website=web_driver.get("https://www.amazon.in/")

web_driver.maximize_window()

WebDriverWait(web_driver,20).until(waitE.visibility_of_element_located((By.XPATH,'//*[@id="nav-xshop"]/a[3]')))

get_prod=web_driver.find_element(By.XPATH,'//*[@id="s-refinements"]/div[1]/ul/li[3]/span/a/span').click()

web_driver.quit()

