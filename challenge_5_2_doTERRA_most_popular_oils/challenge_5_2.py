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

        # Click on 10 most popular essential oils link and validate the URL page
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'https://www.doterra.com/US/en/p/frankincense-oil') and contains(.,'Frankincense oil')]",
                                       "https://www.doterra.com/US/en/p/frankincense-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/lavender-oil') and contains(.,'Lavender oil')]",
                                       "https://www.doterra.com/US/en/p/lavender-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/copaiba-oil') and contains(.,'Copaiba oil')]",
                                       "https://www.doterra.com/US/en/p/copaiba-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/lemon-oil') and contains(.,'Lemon oil')]",
                                       "https://www.doterra.com/US/en/p/lemon-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/wild-orange-oil') and contains(.,'Wild Orange oil')]",
                                       "https://www.doterra.com/US/en/p/wild-orange-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/peppermint-oil') and contains(.,'Peppermint oil')]",
                                       "https://www.doterra.com/US/en/p/peppermint-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/melaleuca-oil') and contains(.,'Tea Tree oil (Melaleuca)')]",
                                       "https://www.doterra.com/US/en/p/melaleuca-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/ginger-oil') and contains(.,'Ginger oil')]",
                                       "https://www.doterra.com/US/en/p/ginger-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/grapefruit-oil') and contains(.,'Grapefruit oil')]",
                                       "https://www.doterra.com/US/en/p/grapefruit-oil")
        Challenge_5_2.element_and_link(self,
                                       "//a[contains(@href,'http://www.doterra.com/US/en/p/eucalyptus-oil') and contains(.,'Eucalyptus oil')]",
                                       "https://www.doterra.com/US/en/p/eucalyptus-oil")


    def element_and_link(self, oil_elm, oil_url):
        oil = self.driver.find_element(By.XPATH, oil_elm)
        oil.click()
        URL = self.driver.current_url
        self.assertEqual(URL, oil_url)
        self.driver.execute_script("window.history.go(-1)")  # back to previous page


if __name__ == '__main__':
    unittest.main()