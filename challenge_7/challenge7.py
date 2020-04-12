import unittest
import time

from pyparsing import unicode
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue
from array import *
import pandas as pd
from html.parser import HTMLParser
from lxml import html
import requests


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_makes_models_array(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

        # Makes / Models
        make_models = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"tabTrending\"]//div[2]")))

        # Print out each car name
        make = make_models.text.split()
        make_url = make_models.get_attribute("innerHTML")

        # This will print all the make html
        for x in make:
            for y in x:
                print(make_url)
            print("\n")

        # ------------------------------------------------------------------
        # Categories
        categories = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"tabTrending\"]/div[3]")))

        # Print out each car name
        category = categories.text.split("\n")
        category_url = categories.get_attribute("innerHTML")

        # This will print all the make html
        for x in category:
            for y in x:
                print(category_url)
            print("\n")

        # Scraper Class
        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                print("Start tag:", tag)

            def handle_endtag(self, tag):
                print("End tag :", tag)

            def handle_data(self, data):
                print("Data:", data)

        #  with open(r'C:\Users\...site_1.html', "r") as f:
        #      page = f.read()
        # tree = make_url.fromstring()

        parser = MyHTMLParser()
        parser.feed(make_url)

        parser2 = MyHTMLParser()
        parser2.feed(category_url)


if __name__ == '__main__':
    unittest.main()