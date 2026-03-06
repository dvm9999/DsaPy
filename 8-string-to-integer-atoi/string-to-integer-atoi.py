class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        res = 0 
        index = 1 if s[0] in "+-" else 0
        sign = -1 if s[0] == '-' else 1
        while index < len(s) and s[index].isdigit():
            res = res * 10 +  ord(s[index]) - ord('0')
            index += 1
        res = res * sign
        return min(2**31 -1, res) if sign == 1 else max(-2**31, res)