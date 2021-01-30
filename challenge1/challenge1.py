import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge1(self):
        #code for our test steps
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    ## Linear Search
    def find_transaction(transactions):
        for index, element in enumerate(transactions):
            if element['device_id'] == '00Z77':
                return index
        return -1

if __name__ == '__main__':
    unittest.main()