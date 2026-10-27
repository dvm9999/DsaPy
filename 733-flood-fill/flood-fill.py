class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        def dfs(i, j, oldc):
            if grid[i][j] == oldc:
                grid[i][j] = color
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < row and 0 <= y < col and grid[x][y] == oldc:
                    dfs(x, y, oldc)
                    
        if grid[sr][sc] != color:
            dfs(sr, sc, grid[sr][sc])
        return grid
