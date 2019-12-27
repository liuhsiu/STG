import time
from selenium.webdriver.common.by import By

class SearchColValue:
    @staticmethod
    def search_col_value(self, table, col_num):
        rows = table.find_elements(By.XPATH, "tr")  # get all of the rows in the table
        text_list = []
        for row in rows:
            col = row.find_elements(By.XPATH, "td" or "td style")[col_num]  # note: index start from 0, 1 is col 2
            #print(col.text)
            text_list.append(col.text)
        return text_list

    def set_unique_list(self, list1):
        print("\r\nTo get the number of occurrences of each item in a list: ")
        print([[l, list1.count(l)] for l in set(list1)], sep="\r\n")

        print("\r\nTo get the number of occurrences of each item in a dictionary: ")
        print((dict((l, list1.count(l)) for l in set(list1))))

        print("\r\nTo get all different types in a row")
        list_row = dict((l, list1.count(l)) for l in set(list1))
        print("\r\n".join(list_row))

        print("\r\nTotal different types of vehicles is: ")
        print("\r\n".len(list_row))
        print("\r\n")


class CountType:
    # @staticmethod
    # def rear_end(self, list):
    #     return 'REAR END'
    # def front_end(self, list):
    #     return 'FRONT END'
    # def minor_dent_scratches(self, list):
    #     return 'MINOR DENT/SCRATCHES'
    # def undercarriage(self, list):
    #     return 'UNDERCARRIAGE'
    # def default(self, list):
    #     print("MISC")
    #     #return not('REAR END') AND ('FRONT END') AND ('MINOR DENT/SCRATCHES') AND ('UNDERCARRIAGE')

    def switch_demo(list1):
        switcher = {
            0: "REAR END",
            1: "FRONT END",
            2: "MINOR DENT/SCRATCHES",
            3: "UNDERCARRIAGE",
            4: "default",
        }
        return (switcher.get(list1, "Invalid vehicle"))



    # # Implement Python Switch Case Statement using Dictionary
    # switcher = {
    #     1: front_end,
    #     2: front_end,
    #     3: minor_dent_scratches,
    #     4: undercarriage,
    # }
    #
    # def switch(item):
    #     return SearchColValue.switcher.get(item, SearchColValue.default)()

