class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revn = 0
        # split the number at middle
        while x > revn:   
            revn = revn * 10 + x % 10
            x //= 10
        # check for even or odd split
        return x == revn or x == revn // 10
        