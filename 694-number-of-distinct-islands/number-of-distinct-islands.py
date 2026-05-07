class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def dfs(r, c, dir):
            nonlocal path_signature
            grid[r][c] = 0
            path_signature += dir
            for x, y, d in [(r + 1, c, "D"), (r - 1, c, "U"),  (r, c + 1, "R"), (r, c - 1, "L")]:
                if 0 <= x < row and 0 <= y < col and grid[x][y]:
                    dfs(x, y, d)            
            path_signature+= "0"      
        
        unique_islands = set()
        path_signature = ""
        for r in range(row):
            for c  in range(col):
                path_signature = ""
                if grid[r][c]: 
                    dfs(r, c, "0")
                    if path_signature:                        
                        unique_islands.add(path_signature)                        
        return len(unique_islands)