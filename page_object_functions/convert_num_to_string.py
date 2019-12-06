import math
class ConvertNumToString:

    @staticmethod
    def convert_num_to_string(number):
        singledigits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

        temp_str = ""
        if number == 0:
                temp_str = "zero"

        first_digit = number // 100000
        second_digit = (number % 100000) // 10000
        third_digit = (number % 10000) // 1000
        fourth_digit = (number % 1000) // 100
        fifth_digit = (number % 100)  // 10
        sixth_digit = (number % 10)

        if first_digit  > 0:
            temp_str = temp_str + singledigits[first_digit] + ' hundred '
        if second_digit >= 0:
            temp_str = temp_str + tens[second_digit] + ' '
        if third_digit >= 0:
            temp_str = temp_str + singledigits[third_digit] + 'thousand '
        if fourth_digit > 1:
            temp_str = temp_str + singledigits[fourth_digit] + ' hundred '
        if fifth_digit > 1:
            temp_str = temp_str + tens[fifth_digit] + ' '
        if sixth_digit > 0:
            temp_str = temp_str + singledigits[sixth_digit]

        else:
            if temp_str[-1] == " ":  # If the last number is a space
                temp_str = temp_str[0:-1]  # Slice it
        return temp_str