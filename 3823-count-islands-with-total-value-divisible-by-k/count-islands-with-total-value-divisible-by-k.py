class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:    
        row, col = len(grid), len(grid[0])
        def dfs(x, y):
            nonlocal total
            total += grid[x][y]
            grid[x][y] *= -1
            for a,b in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)] :
                if 0 <= a < row and 0 <= b < col  and  grid[a][b] > 0 :
                    dfs(a,b) 
        total, ans  = 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] > 0:
                    total = 0
                    dfs(r, c)
                    ans += total % k == 0
        return ans