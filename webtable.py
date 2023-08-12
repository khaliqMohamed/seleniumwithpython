
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

driver.get("file:///C:/Users/khali/OneDrive/Desktop/newsapp/table.html")

time.sleep(5)

rows=len(driver.find_elements(By.XPATH,'//html/body/table/tbody/tr')) #count no.of.rows
cols=len(driver.find_elements(By.XPATH,'//html/body/table/tbody/tr[1]/th')) #count no.of.cols


print(rows)
print(cols)
print("name"+"     "+"roll no"+"     "+"status" )      #just hardcode the column name bcoz in our for loop it doesn't take


for r in range(2,rows+1): #retrive from 2nd rows exclude 1st row
   for c in range(1,cols+1): #retrieve from 1st column 
        val=driver.find_element(By.XPATH,'//html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]').text
        print(val,end="  ")
print()

driver.quit()


