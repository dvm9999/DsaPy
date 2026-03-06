class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shorteststr =  min(strs, key = len)
        for i, c in enumerate(shorteststr):
            for str in strs:
                if str[i] != c:
                    return shorteststr[:i]
        return shorteststr
    