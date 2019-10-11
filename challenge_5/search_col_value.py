from selenium.webdriver.common.by import By

class SearchColValue:
    @staticmethod
    def search_col_value(table, col_num):
        rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
            col = row.find_elements(By.TAG_NAME, "td")[col_num]  # note: index start from 0, 1 is col 2
            # prints text from the element
            print(col.text)

    #convert string to list
    def Convert(string):
        li = list(string.split(" "))
        return li