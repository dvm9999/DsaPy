class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    perimeter += 4
                    if r and grid[r - 1][c]:
                        perimeter -= 2
                    if c and grid[r][c - 1]:
                        perimeter -= 2
        return perimeter
        