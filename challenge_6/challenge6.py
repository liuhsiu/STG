import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue
from PIL import Image, ImageFile


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

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


        # When the link does not exist to click on, your script will throw an exception.
        try:
            # Load an image from the hard drive
            original = Image.open("Lenna.png")

            # Blur the image
            blurred = original.filter(ImageFilter.BLUR)

            # Display both images
            original.show()
            blurred.show()

            # save the new image
            blurred.save("blurred.png")

        except:
            print("Unable to load image")

        #myimage.load()

        # -------------------------------------------------------------------------------
        #  Catch the exception and take a screenshot of the page of what it looks like.
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "/usr/bin/chromium"
        driver = webdriver.Chrome(chrome_options=options)

        driver.get('https://python.org')
        driver.save_screenshot("screenshot.png")

        driver.close()


        # -------------------------------------------------------------------------------
        # Capture screenshot of an Element
        driver = webdriver.Firefox(executable_path='[Browser Driver Path]');
        driver.get('https://www.google.co.in');
        element = driver.find_element_by_xpath("//div[@id='hplogo']");

        location = element.location;
        size = element.size;

        driver.save_screenshot("/data/image.png");

        x = location['x'];
        y = location['y'];
        width = location['x'] + size['width'];
        height = location['y'] + size['height'];

        im = Image.open('/data/WorkArea/image.png')
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save('/data/image.png')





        # def FlipState(self):
        #     self.test = self.CheckMode.get()
        #     if self.test == 1:  # checked
        #         self.input_box['state'] = DISABLED
        #     elif self.test == 0:  # unchecked
        #         self.input_box['state'] = NORMAL


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