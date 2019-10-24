import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue


class Challenge_5_3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    # Validate all the URLs in the footer
    # Figure out how many of the products have the word doTERRA in it, how may are DigestZens and how many fit into a misc category.
    def test_doTERRA_footer_all_URL(self):
        self.driver.get("https://www.doterra.com/US/en/product-education-blends")
        self.driver.maximize_window()

        # Scoll down to the bottom of the page
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True




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

        # -----------------------------------------------------------------------------------------
        # return in the terminal how many of each type exists.
        # Possible values can be “CAYENNE S”, “BOXSTER S”, etc.
        # get values from model column

        model_col_num = 5
        model = SearchColValue()
        model_list = model.search_col_value(self, serverSideDataTable, model_col_num)
        print(model_list)

        #Count how many different models of porsche is in the results on the first page
        SearchColValue.set_unique_list(self, model_list)

        # get values from damage column
        damage_col_num = 11
        damage = SearchColValue()

        # Count how many different damage of porsche is in the results on the first page
        damage_list = damage.search_col_value(self, serverSideDataTable, damage_col_num)
        print(damage_list)

        SearchColValue.set_unique_list(self, damage_list)

        # For the 2nd part of this challenge, create a switch statement to count the types of damages
        # Here's the types:
        # REAR END
        # FRONT END
        # MINOR DENT/SCRATCHIES
        # UNDERCARRIAGE
        # AND ANY OTHER TYPES CAN BE GROUPED INTO ONE OF MISC.

        SearchColValue.damage_type(self, damage)


if __name__ == '__main__':
    unittest.main()