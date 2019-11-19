import unittest, sys, pyautogui
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

        searchfilterInput = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"collapseinside4\"]/form/div/input")))
        searchfilterInput.send_keys("skyline" + Keys.ENTER)

        time.sleep(3)

        skylineCheckBox = self.driver.find_element(By.XPATH, "//*[@id=\"lot_model_descSKYLINE\"]")
        skylineCheckBox.click()

        try:
            print(CheckURLToJPG.existsURL(
                'https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX197/b1e084be-90bb-4709-aca0-2f1691105a9a.JPG'))
            print(CheckURLToJPG.existsURL(
                'https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX206/6d8a784f-13e3-4447-9571-62c5d5dffae1.JPG'))

        except:
            print("images are not same")

            #myimage.load()
            # -------------------------------------------------------------------------------
            #  Catch the exception and take a screenshot of the page of what it looks like.
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("--test-type")
            #options.binary_location = "/usr/bin/chromium"
            driver = webdriver.Chrome(chrome_options=options)

            #driver.get('https://python.org')
            #im1 = Image.open(r"C:\Users\clee1\Desktop\image1.jpg")
            im1 = Image.open(r"C:\Users\clee1\Desktop")
            im1 = im1.save("image1.jpg")
            driver.save_screenshot("screenshot.png")
            driver.close()

            # import math, operator
            # from PIL import Image
            # def compare(file1, file2):
            #     image1 = Image.open("/home/pi/Desktop/1.jpg)
            #     image2 = Image.open("/home/pi/Desktop/2.jpg")
            #     h1 = image1.histogram()
            #     h2 = image2.histogram()
            #     rms = math.sqrt(reduce(operator.add,
            #                            map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
            #     return rms
            #
            # if __name__ == '__main__':
            #     import sys
            #     file1, file2 = sys.argv[1:]
            #     print
            #     compare(file1, file2)



        # # -------------------------------------------------------------------------------
        # # Capture screenshot of an Element
        # driver = webdriver.Firefox(executable_path='[Browser Driver Path]');
        # driver.get('https://www.google.co.in');
        # element = driver.find_element_by_xpath("//div[@id='hplogo']");
        #
        # location = element.location;
        # size = element.size;
        #
        # driver.save_screenshot("/data/image.png");
        #
        # x = location['x'];
        # y = location['y'];
        # width = location['x'] + size['width'];
        # height = location['y'] + size['height'];
        #
        # im = Image.open('/data/WorkArea/image.png')
        # im = im.crop((int(x), int(y), int(width), int(height)))
        # im.save('/data/image.png')





        # def FlipState(self):
        #     self.test = self.CheckMode.get()
        #     if self.test == 1:  # checked
        #         self.input_box['state'] = DISABLED
        #     elif self.test == 0:  # unchecked
        #         self.input_box['state'] = NORMAL


        #


if __name__ == '__main__':
    unittest.main()