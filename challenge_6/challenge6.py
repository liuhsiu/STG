import unittest, sys, pyautogui
import urllib
import lxml.html
import time
import PIL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue
from page_object_functions.verify_image import CheckURLToJPG
from PIL import Image, ImageFile


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')
        # type, value, traceback = sys.exc_info()
        # if type is exceptions.AssertionError:
        #     self.driver.save_screenshot(r'screenshot-failure.png')
        # elif type is exceptions.Exception:
        #     self.driver.save_screenshot(r'screenshot-error.png')

        self.driver.close()
        print('in tear down method')

    def screenshot(self, func):
        def screenshot_exception(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                self.driver.save_screenshot('{0}/{1}.jpeg'.format(screenshot_dir, self.id()))
                raise

        return screenshot_exception

    def test_error_handling(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("nissan" + Keys.ENTER)
        table = WebDriverWait(self.driver, 60).until(
             EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
        time.sleep(3)
        html = table.get_attribute("innerHTML")
        # print(html)
        self.assertIn("nissan", html)
        searchfield.send_keys(Keys.ENTER)
        time.sleep(3)
        modelFilter = self.driver.find_element(By.XPATH, "//*[@id=\"filters-collapse-1\"]/div[1]/ul/li[4]/h4/a[1]")
        modelFilter.click()

        try:
            searchfilterInput = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"collapseinside4\"]/form/div/input")))
            searchfilterInput.send_keys("skyline" + Keys.ENTER)

            time.sleep(3)

            skylineCheckBox = self.driver.find_element(By.XPATH, "//*[@id=\"lot_model_descSKYLINE\"]")
            skylineCheckBox.click()

            # Array or List or Dictionary to store how many vehicles,
            serverSideDataTable = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]/tbody")))

            model_col_num = 5
            model = SearchColValue()
            model_list = model.search_col_value(self, serverSideDataTable, model_col_num)
            print(model_list)

            # Count how many different models of porsche is in the results on the first page
            SearchColValue.set_unique_list(self, model_list)

        except:
            self.driver.save_screenshot("screenshot.png")
            self.driver.close()
            #assert False, "image are not same"  # At least one vehicles exist then pass


if __name__ == '__main__':
    unittest.main()