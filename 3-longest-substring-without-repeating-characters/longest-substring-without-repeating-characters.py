class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        uniquechars = set()
        left, ans = 0,  0       
        for right in range(len(s)):
            while left < right and s[right] in uniquechars:
                uniquechars.remove(s[left])
                left += 1
            uniquechars.add(s[right])
            ans = max(ans, len(uniquechars))
        return ans
