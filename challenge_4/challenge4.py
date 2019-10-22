import unittest

from page_object_functions.recur_fibo import RecurFibo
from page_object_functions.convert_num_to_string import ConvertNumToString



class Challenge4(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #
    # def tearDown(self):
    #     self.driver.close()
    #     print('in tear down method')

    # def test_for_loop(self):
    #     self.driver.get("https://www.copart.com")
    #     popsearches = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
    #     #popsearches = self.driver.find_element(By.XPATH, "//*[@id='tabTrending']/div[1]")
    #     print(len(popsearches))
    #     for x in popsearches:
    #         print(x.text + "-" + x.get_attribute("href"))
    #
    # def test_while_loop(self):
    #     popcategories = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]/../div[3]//a")
    #     i = 0
    #     while i < len(popcategories):
    #         print(i)
    #         i += 1
    #         print(popcategories.index[i].text + "-" + popcategories[i].get_attribute("href"))



    # Program to display the Fibonacci sequence up to n-th term where n is provided by the user
    def test_recur_fibo(self):

        # Change this value for a different result
        #nterms = 10
        #Fibonacci.recur_fibo(nterms)

        # uncomment to take input from the user
        nterms = int(input("How many terms? "))

        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        else:
            print("Fibonacci sequence:")
            for i in range(nterms):
                print(RecurFibo.recur_fibo(i))
        # Output 0, 1, 1, 2, 3, 5, 8, 13, 21, if is 9 terms

    def test_convert_num_to_string(self):
        num = int(input("Please enter a positive integer: "))
        print("The number is " + str(num))

        # don't delete this line, using map() to convert number to list of integers
        # res = list(map(int, str(num)))

        # using list comprehension to convert number to list of integers
        res = [int(i) for i in str(num)]
        print("The list from number is " + str(res))

        # Convert a number to single string

        s = ConvertNumToString()
        single_string = s.convert_num_to_string(num)
        print(str(num) + " - " + single_string)

if __name__ == '__main__':
    unittest.main()