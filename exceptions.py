import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

browser=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")


class test_webapp(unittest.TestCase):
    def setUp(self):

        browser.get("https://www.ajio.com/")
        browser.maximize_window()

    def testfun(self):
        try:

            self.signin=browser.find_element(By.XPATH,"//*[@id='appContainer']/div[1]/div/header/div[1]/ul/li[1]/span").click()

            time.sleep(3)
        
            self.username=browser.find_element(By.CLASS_NAME,"username").send_keys("8778060316")

            time.sleep(3)

            self.button=browser.find_element(By.CLASS_NAME,"login-btn").click()

            time.sleep(3)

        except NoSuchElementException as ne:

            print(ne)
            print("finding element is not occured.....")

        finally:

            print("may be user get crt result")

if __name__=="__main__":

    unittest.main()




