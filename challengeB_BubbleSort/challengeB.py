import unittest, sys, pyautogui
import urllib
import lxml.html
import time
# from util import time_it  # put time_it in the util file, need to create one
import PIL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from page_object_functions.search_col_value import SearchColValue
from page_object_functions.verify_image import CheckURLToJPG
from PIL import Image, ImageFile

class ChallengeB(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        #code to close webdriver
        self.driver.close()
        print('in tear down method')

    def test_challengeB_BubbleSort(self):
        #code for our test steps
        # self.driver.get("https://www.google.com")
        # self.assertIn("Google", self.driver.title)
        number_list_1 = [12, 15, 17, 19, 21, 24, 45, 67]
        #number_to_find = 9808  # will return -1 because cannot find it
        number_to_find_1 = 24

        # if we use big number to search and check what's different with performance for linear search and binary search with time.
        # Binary search of course is faster
        number_list_2 = [i for i in range(1000001)]
        number_to_find = 1000000  # need to test all the numbers, 12, 67, 21, etc.


        index = linear_search(number_list, number_to_find)  # not sure why this function has problem, solve it.....
        print(f"Number found at index {index} using linear serach")

        index = binary_search(number_list, number_to_find)
        print(f"Number found at index {index} using binary serach")

    # Solve the following problem:
    # 1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index, why is that?'
    #     number = [1, 4, 6, 9, 10, 6, 7]
    #
    # 2. Find index of all the occurances of a number from sorted list
    #     number = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    #     number_to_find = 15
    #
    # This shoud return 5,6, 7 as indices containing number 15 in the array


    ## Linear Search
    def find_transaction(transactions):
        for index, element in enumerate(transactions):
            if element['device_id'] == '00Z77':
                return index
        return -1

    ## Binary Search
    ## Iteration 1 = n/2
    ## Iteration 2 = (n/2)/2 = n/2^2
    ## Iteration 3 = (n/2^2)/2 = n/2^3
    ## Iteration k = n/2^k
    ## l = n/2^k
    ## n = 2^k
    ## log2 n = log2 2^k
    ## log2 n= k * log2 2
    ## K = log n   ===>  O(log n)
    ## Linear Search is  O(n)
    ## Binary Search is  Log(n)


    def linear_search(numbers_list, number_to_find):
        for index, element in enumerate(numbers_list):
            if element == number_to_find:
                return index
        return -1

    def binary_search(numbers_list, number_to_find):
        left_index = 0
        right_index = len(numbers_list) - 1
        mid_index = 0

        while left_index <= right_index
            mid_index = (left_index + right_index) // 2  # devide by 2 should use //
            mid_number = numbers_list[mid_index]

            if mid_number == number_to_find:
                return mid_index

            if mid_number < number_to_find
                left_index = mid_index + 1
            else:
                right_index = mid_index -1

        return -1


    def time_it(func):
        def wrapper(*args, **kwags):
            start = time.time()
            result = func(*args, **kwags)
            end = time.time()
            print(func.__name__ + " took " + str((end-start)*1000) + " mil sec")
            return result
        return wrapper

    def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
        if right_index < left_index:
            return -1

        mid_index = (left_index + right_index) // 2  # devide by 2 should use //
        if mid_index >= len(numbers_list) or mid_index < 0:
            return -1

        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_number

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

        return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)  # recursive function has no loop


if __name__ == '__main__':
    unittest.main()