from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get("https://www.selenium.dev/")

loc_another_page=driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/div/a").click()

print(driver.current_window_handle)  #to print parent window id by default browser handle current window

handles=driver.window_handles # to retrieve all windows id handle by the browser

for handle in handles:  #to get the all windows
    driver.switch_to.window(handle) #to switch the windows
    print(driver.title) #print the title

    if driver.title=="Selenium":  #if the window is selenium then it will be closed
        driver.close()


driver.quit()