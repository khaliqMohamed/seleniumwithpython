import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class testcaserunner(unittest.TestCase):

    def setUp(self):

        self.browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
       
        self.browser.maximize_window
    
    def tearDown(self):
        self.browser.quit()

    def test_homepage(self):

        self.browser.get("https://www.ajio.com/")
        assert self.browser.title=="ajio"

    def test_login(self):

        self.browser.get("https://www.ajio.com/")
        self.browser.find_element(By.XPATH,'//*[@id="appContainer"]/div[1]/div/header/div[1]/ul/li[1]/span').click()
        self.browser.find_element(By.XPATH,'//*[@id="login-modal"]/div/div/div[2]/div/form/div[2]/div[1]/label/input').send_keys("abc@text.com")
        self.browser.find_element(By.CLASS_NAME,"login-btn").click()
        assert self.browser.title=="ajio"

if __name__=="__main__":
    unittest.main()   



        