import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SearchColValue:

    @staticmethod
    def search_col_value(table, col_num):
    #model_col = 5
        rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
        # Get the columns (all the column 2)
            col = row.find_elements(By.TAG_NAME, "td")[col_num]  # note: index start from 0, 1 is col 2
            print(col.text)  # prints text from the element
