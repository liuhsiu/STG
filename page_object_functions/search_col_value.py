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

        # print("\r\nTotal different types of vehicles is: ")
        # #print("\r\n".len(list_row))
        # print("\r\n")


class CountType:
    #@staticmethod
    def rear_end(self, list1):
        return "REAR END"
    def front_end(self,list1):
        return "FRONT END"
    def minor_dent_scratches(self,list1):
        return "MINOR DENT/SCRATCHES"
    def undercarriage(self,list1):
        return "UNDERCARRIAGE"
    def default(self,list1):
        return "MISC"
        #return not (('REAR END'), ('FRONT END'), ('MINOR DENT/SCRATCHES'), ('UNDERCARRIAGE'))

    switcher = {
        1: rear_end,
        2: front_end,
        3: minor_dent_scratches,
        4: undercarriage
        }

    # ------------------------------------------------------------------------------
    # def monday(self):
    #     return "monday"
    #
    # def tuesday(self):
    #     return "tuesday"
    #
    # def wednesday(self):
    #     return "wednesday"
    #
    # def thursday(self):
    #     return "thursday"
    #
    # def friday(self):
    #     return "friday"
    #
    # def saturday(self):
    #     return "saturday"
    #
    # def sunday(self):
    #     return "sunday"
    #
    # def default(self):
    #     return "Incorrect day"
    #
    # switcher = {
    #     1: monday,
    #     2: tuesday,
    #     3: wednesday,
    #     4: thursday,
    #     5: friday,
    #     6: saturday,
    #     7: sunday
    # }
