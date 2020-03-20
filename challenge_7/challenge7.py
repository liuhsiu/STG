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
        #makes_models = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]")
        #print(len(makes_models))

        #rows = table.find_elements(By.XPATH, "tr")  # get all of the rows in the table

        #make_col = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]/div[1]/ul/li[1]")
        make_row = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]")

        # make_col
        # // *[ @ id = "tabTrending"] / div[1] / div[2] / div[1] / ul
        # // *[ @ id = "tabTrending"] / div[1] / div[2] / div[2] / ul
        # // *[ @ id = "tabTrending"] / div[1] / div[2] / div[3] / ul
        # // *[ @ id = "tabTrending"] / div[1] / div[2] / div[4] / ul

        #make_row, make_col = (5, 4)
        #arr = [[0 for i in range(make_row)] for j in range(make_row)]

        # col_num = 0
        #
        # text_list = []
        # for row in make_col:
        #     col = row.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]/div[2]")[col_num]  # note: index start from 0, 1 is col 2
        #     print(col.text)
        #     text_list.append(col.text)
        # return text_list

        x = []
        for x in make_row:
            try:
                print(x.text)  # Return type none
                print(x.text + "-" + x.get_attribute("href"))  # Return type none
            except:
                print("x didn't have attribute")



if __name__ == '__main__':
    unittest.main()