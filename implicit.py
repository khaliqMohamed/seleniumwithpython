from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

#open chrome browser
get_brow=webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

#wait for 10 sec if it fetch that particular element for all
get_brow.implicitly_wait(10)

#open ajio website
get_brow.get("https://www.ajio.com/")

#maximize window
get_brow.maximize_window()

#click sign in
get_brow.find_element(By.XPATH,'//*[@id="appContainer"]/div[1]/div/header/div[1]/ul/li[1]/span').click()

#put mobile number
get_brow.find_element(By.XPATH,'//*[@id="login-modal"]/div/div/div[2]/div/form/div[2]/div[1]/label/input').send_keys("8778060316")

#click continue process
get_brow.find_element(By.XPATH,'//div/input[@value="Continue"]').click()

#click gender option
radiobutton=get_brow.find_element(By.XPATH,'//*[@id="login-modal"]/div/div/div[2]/div/div/div[2]/form/div[3]/label[2]/span').click()

#put name in name textbox
name=get_brow.find_element(By.XPATH,'//div/input[@placeholder="Name"]').send_keys("khaliq")

#put email id in email id text box
email=get_brow.find_element(By.XPATH,'//div/input[@placeholder="Email"]').send_keys("khaliqmohamedm@gmail.com")

#put password in password text box
pwd=get_brow.find_element(By.XPATH,'//div/input[@placeholder="Password"]').send_keys("1234khaliq2001")

#put code in invite code text box
invite_code=get_brow.find_element(By.XPATH,'//*[@id="login-modal"]/div/div/div[2]/div/div/div[2]/form/div[11]/input').send_keys("AKWSDEY")

#click checkbox
check_box=get_brow.find_element(By.XPATH,'//*[@id="login-modal"]/div/div/div[2]/div/div/div[2]/form/div[12]/label/input').click()

print(get_brow.current_url)

get_brow.get_screenshot_as_file("ajio.png")
#close the broswer
get_brow.quit()