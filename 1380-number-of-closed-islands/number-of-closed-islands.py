class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        closedIslandCount = 0
        def dfs(i, j):
            grid[i][j] = 2
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < row and 0 <= y < col and not grid[x][y]:
                    dfs(x, y)
        
        
        for r in [0, row -1]:
            for c in range(col):
                if not grid[r][c]:
                    dfs(r, c)
        for c in [0, col - 1]:
            for r in range(row):
                if not grid[r][c]:
                    dfs(r, c)
        for r in range(1, row - 1):
            for c in range(1, col - 1):
                if not grid[r][c]:
                    closedIslandCount += 1
                    dfs(r, c)
                    
        return closedIslandCount