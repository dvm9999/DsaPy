class Solution:
    def intToRoman(self, num: int) -> str:
        itor = {1: 'I', 4: 'IV', 5:'V', 9: 'IX',  10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M' }
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        index = 0
        roman = ""
        while num:
            while val[index] <= num:
                roman += itor[val[index]]
                num -= val[index]
            index += 1
        return roman 
            
