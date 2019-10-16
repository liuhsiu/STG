class ConvertNumToString:

    @staticmethod
    def convert_num_to_string(n):
        def getNumber(num):
            return num

        singledigits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        tens = ["", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        # 400 four hundred +
        # secondval = 5 fifty +
        # leastsignal = 1

        # print (singledigits[leastsignal]) => one
        # print (tens[secondval] + singledigits[leastsignal]) => fifty one

        # 105 one hundred five million
        # 105 one hundred five thousand
        # 105 one hundred five
        #




