class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) ^ (divisor < 0)        
        dividend, divisor = abs(dividend), abs(divisor)       
        quotient = 0
        factor = 1
        while factor * divisor <= dividend:
            quotient += factor
            dividend -=  factor * divisor
            factor *= 2
            if factor * divisor > dividend:
                factor = 1
        return max(-(2 **31) , -quotient ) if sign else min( 2 **31 -1  , quotient)






        