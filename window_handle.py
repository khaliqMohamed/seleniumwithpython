import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class test_web(unittest.TestCase):

    applnname="https://www.makemytrip.com/"

    def setUp(self):
        self.web_page=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
        self.web_page.get(self.applnname)
        time.sleep(7)

    def tearDown(self):
        self.web_page.quit()

    def test_web(self):
        self.web_page.find_element(By.XPATH,'//*[@id="superOffersTab_BANK_OFFERS"]/span').click()

if __name__=="__main__":
    unittest.main()

