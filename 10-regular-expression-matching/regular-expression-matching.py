class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                memo[i, j]  = i == len(s)
            else:
                first_match = i < len(s) and p[j] in s[i] + '.'
                if j + 1 < len(p) and p[j + 1] == '*':
                    memo[i,j]= dfs(i, j + 2) or first_match and dfs(i + 1, j)
                else:
                    memo[i, j]= first_match and dfs(i + 1, j + 1)                
            return memo[i, j]
        return dfs(0, 0)