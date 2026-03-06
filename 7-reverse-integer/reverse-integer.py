class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x, res  = abs(x), 0        
        while x:
            x, r  = divmod(x, 10)
            res = res * 10 +  r            
            if res > 2**31 - 1:
                return 0            
        return res * sign
                 