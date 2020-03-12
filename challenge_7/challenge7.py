import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_makes_models_array(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

        #makes_models = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]")
        makes_models = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]")
        print(len(makes_models))

        for x in makes_models:
            print(x.text + "-" + x.get_attribute("href"))  # Return type none



if __name__ == '__main__':
    unittest.main()