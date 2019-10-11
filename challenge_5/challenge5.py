import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from challenge_5.search_col_value import SearchColValue
from challenge_5.unique_list import UniqueList
from collections import Counter


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_show_model_entries_100(self):
        self.driver.get("https://www.copart.com")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("PORSCHE" + Keys.ENTER)
        table = WebDriverWait(self.driver, 60).until(
             EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
        time.sleep(3)
        html = table.get_attribute("innerHTML")
        # print(html)
        self.assertIn("PORSCHE", html)
        searchfield.send_keys(Keys.ENTER)

        # Search for “porsche” and change the drop down for “Show Entries” to 100 from 20.
        showentries = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_length\"]/label/select")))
        showentries.click()
        showentries.send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(5)

        serverSideDataTable = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody")))

        # get values from model column
        model_col = 5
        model_list = SearchColValue.search_col_value(serverSideDataTable, model_col)
        print(model_list)

        #Count how many different models of porsche is in the results on the first page
        unique_models = set(model_list)
        unique_model_count = len(SearchColValue.search_col_value(serverSideDataTable, unique_models))
        print(unique_model_count)

        # return in the terminal how many of each type exists.
        # Possible values can be “CAYENNE S”, “BOXSTER S”, etc.

        # -----------------------------------------------------------------------------------------
        # get values from damage column
        damage_col = 11
        damage_list = SearchColValue.search_col_value(serverSideDataTable, damage_col)
        print(damage_list)










if __name__ == '__main__':
    unittest.main()