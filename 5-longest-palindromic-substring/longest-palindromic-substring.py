''' manacher algo:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        P = [0] * n
        C = R = 0    
        max_len = 0
        center_idx = 0
        for i in range(1, n - 1):
            if i <= R:
                i_mirror = 2 * C - i
                P[i] = min(P[i_mirror], R - i)
            while t[i - (P[i] + 1)] == t[i + P[i] + 1]:
                P[i] += 1
            if i + P[i] > R:
                R = i + P[i]
                C = i
            if P[i] > max_len:
                max_len = P[i]
                center_idx = i
        start = (center_idx - max_len) // 2
        end = start + max_len
        return s[start:end]
    '''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = -1
        res = ""
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen, res = r - l + 1, s[l: r + 1]
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen, res = r - l + 1, s[l: r + 1]
                l -= 1
                r += 1
        return res
        