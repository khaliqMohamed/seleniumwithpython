import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.get("https://www.amazon.in/")

path="D:\selenium\data.xlsx"

rows=XLUtils.getrowcount(path)

for r in range(2,rows+1):

    username=XLUtils.readdata(path,r,1)
    password=XLUtils.readdata(path,r,2)

    driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a').click()
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys(username)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button/span').click()

    if driver.title=="Flipkart : product":
        print("test passed")
        XLUtils.writedata(path,r,3,"test passed")

    else:
        print("test failed")
        XLUtils.writedata(path,r,3,"test failed")

    
driver.quit()