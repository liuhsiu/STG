import math
class ConvertNumToString:

    @staticmethod
    def convert_num_to_string(number):
        singledigits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

        temp_str = ""
        if number == 0:
                temp_str = "zero"

        first_digit = number // 1000
        second_digit = (number % 1000) // 100
        third_digit = (number % 100) // 10
        fourth_digit = (number % 10)

        if first_digit  > 0:
            temp_str = temp_str + singledigits[first_digit] + ' thousand '
        if second_digit > 0:
            temp_str = temp_str + singledigits[second_digit] + ' hundred and '
        if third_digit > 1:
            temp_str = temp_str + tens[third_digit] + " "
        if third_digit == 1:
            temp_str = temp_str + teens[fourth_digit] + " "
        else:
            if fourth_digit:
                temp_str = temp_str + singledigits[fourth_digit] + " "
            if temp_str[-1] == " ":  # If the last number is a space
                temp_str = temp_str[0:-1]  # Slice it
        return temp_str

