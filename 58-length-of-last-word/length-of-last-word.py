class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.rstrip().split(" ")
        return len(ls[-1])

        