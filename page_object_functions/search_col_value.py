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

        print("\r\nTotal different types of the items is: ")
        print(len(list_row))
        print("\r\n")

    # Implement Python Switch Case Statement using Dictionary
    def damage_type(self, list1):
        def rear_end():
            x = dict((l, list1.count(l)) for l in set(list1))
            return x
        def front_end():
            return "FRONT END"
        def minor_dent_scratchies():
            return "MINOR DENT/SCRATCHIES"
        def undercarriage():
            return "UNDERCARRIAGE"
        def default():
            return "MISC"

        switcher = {
            1: rear_end,
            2: front_end,
            3: minor_dent_scratchies,
            4: undercarriage,
        }
        return(switcher.get(list1, default))
