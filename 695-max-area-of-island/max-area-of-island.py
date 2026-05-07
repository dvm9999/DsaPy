class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal curr_area
            grid[i][j] = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < row and 0 <= y < col and grid[x][y]:
                    dfs(x, y)
                    curr_area += 1

        curr_area, max_area = 0, 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    curr_area = 1
                    dfs(r, c)
                    max_area = max(max_area, curr_area)                           
        return max_area