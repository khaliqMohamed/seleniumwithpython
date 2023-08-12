from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
browser.get("https://www.flipkart.com/")

browser.maximize_window()

time.sleep(2)

login=browser.find_element(By.XPATH,'//div[@tabindex=-1]/div/button').click()

time.sleep(2)

travel_list=browser.find_element(By.XPATH,'//div[@class="xtXmba" and text()="Travel"]').click()

time.sleep(2)

source=browser.find_element(By.CSS_SELECTOR,("input[name='0-departcity']")).click()

time.sleep(2)


# source_dropdown=Select(source)

# time.sleep(10)

source_dropdown=browser.find_element(By.XPATH,'//span[text()="Mumbai"]').click()

time.sleep(3)

destination=browser.find_element(By.XPATH,"//*[@id='container']/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/div[1]/div[1]/input").click()

time.sleep(4)

#dest_dd=browser.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/div[1]/div[1]/input').send_keys("Kerala")

search=browser.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div[1]/div/div[2]/div/div[2]/form/div/button/span').click()

time.sleep(2)
# time.sleep(10)

# search_but=browser.find_element(By.XPATH,'//button[@tabindex="05"]').click()

# select_source=source_dropdown.options()

# for opt in source_dropdown.options:
#     source_dropdown.select_by_visible_text(opt.get_attribute('Mumbai'))


#time.sleep(4)
# destination=browser.find_element(By.XPATH,'//input[@tabindex=02]').click()

# time.sleep(8)

# dest_drop=Select(destination)

# dest_drop.select_by_value('Hyderabad,IN')

print(browser.current_url)

browser.quit()
