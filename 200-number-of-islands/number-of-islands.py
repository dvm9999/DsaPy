class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == "1":
                grid[i][j] = '0'
            for x, y in [(i + 1, j), ( i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                    dfs(x, y)
        noOfIslands  = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    noOfIslands += 1
                    dfs(r, c)
        return noOfIslands