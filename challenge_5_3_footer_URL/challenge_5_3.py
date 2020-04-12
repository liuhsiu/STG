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


if __name__ == '__main__':
    unittest.main()