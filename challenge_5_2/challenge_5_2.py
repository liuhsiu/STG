import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue


class Challenge_5_2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_doTERRA_10_most_popular_oils(self):
        self.driver.get("https://www.doterra.com/US/en/using-essential-oils")
        self.driver.maximize_window()

        # Scoll down to 10 most popular essential oils
        most_10_popular_essential_oils = self.driver.find_element(By.XPATH, "//*[@id=\"content_body\"]/div/div[1]/div/p[13]/strong")
        view_port_height = "var viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);"
        element_top = "var elementTop = arguments[0].getBoundingClientRect().top;"
        js_function = "window.scrollBy(0, elementTop-(viewPortHeight/2));"

        scroll_into_middle = view_port_height + element_top + js_function
        self.driver.execute_script(scroll_into_middle, most_10_popular_essential_oils)

        frankincense_oil = self.driver.find_element(By.XPATH, "//a[contains(@href,'https://www.doterra.com/US/en/p/frankincense-oil') and contains(.,'Frankincense oil')]")
        frankincense_oil.click()

        frankincense_oil_url = "https://www.doterra.com/US/en/p/frankincense-oil"
        URL = self.driver.current_url

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, frankincense_oil_url)))
            not_found = False
        except:
            not_found = True

        assert not_found


if __name__ == '__main__':
    unittest.main()