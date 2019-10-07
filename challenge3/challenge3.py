import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_for_loop(self):
        self.driver.get("https://www.copart.com")
        popsearches = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        #popsearches = self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]")
        print(len(popsearches))
        for x in popsearches:
            print(x.text + "-" + x.get_attribute("href"))

    def test_while_loop(self):
        popcategories = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
        i = 0
        while i < len(popcategories):
            print(i)
            i += 1
            print(popcategories.index[i].text + "-" + popcategories[i].get_attribute("href"))


if __name__ == '__main__':
    unittest.main()