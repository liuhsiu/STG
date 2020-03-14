import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue
from functools import partial
#from page_object_functions.search_col_value import CountType


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_show_model_100_entries(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("PORSCHE" + Keys.ENTER)
        table = WebDriverWait(self.driver, 60).until(
             EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
        time.sleep(3)
        html = table.get_attribute("innerHTML")
        # print(html)
        self.assertIn("PORSCHE", html)
        searchfield.send_keys(Keys.ENTER)

        #Change the drop down for “Show Entries” to 100 from 20.
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

        print('\n\nTo create a switch statement to count the types of damages')

        # damage dictionary
        damage_type = dict((l, damage_list.count(l))
                         for l in set(damage_list))

        exclude_type = {'REAR END', 'FRONT END', 'MINOR DENT/SCRATCHES', 'UNDERCARRIAGE'}

        misc_type = {x: damage_type[x] for x in damage_type
                     if x not in exclude_type}

        def rear_one(damage_type_disc):
            return f"REAR END: {damage_type_disc['REAR END']}"

        def front_end(damage_type_disc):
            return f"FRONT END: {damage_type_disc['FRONT END']}"

        def minor_dent_scratches(damage_type_disc):
            return f"MINOR DENT/SCRATCHES: {damage_type_disc['MINOR DENT/SCRATCHES']}"

        def undercarriage(damage_type_disc):
            return f"UNDERCARRIAGE: {damage_type_disc['UNDERCARRIAGE']}"

        def default(misc_type_disc):
            return f"MISC: {misc_type_disc}"

        def count_type(argument, damage_type_disc):
            switcher = {
                1: partial(rear_one, damage_type_disc),
                2: partial(front_end, damage_type_disc),
                3: partial(minor_dent_scratches, damage_type_disc),
                4: partial(undercarriage, damage_type_disc),
                5: partial(default, damage_type_disc)
            }
            # Get the function from switcher dictionary
            func = switcher.get(argument, lambda: default(damage_type_disc))
            print(func())

        count_type(1, damage_type)
        count_type(2, damage_type)
        count_type(3, damage_type)
        count_type(4, damage_type)
        count_type(5, misc_type)


if __name__ == '__main__':
    unittest.main()