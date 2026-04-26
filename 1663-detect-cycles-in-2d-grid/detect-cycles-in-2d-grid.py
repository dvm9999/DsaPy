class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        def bfs(i, j , c):
            visited.add((i, j))
            q = deque([(i, j, -1, -1)])
            while(q):
                x, y, px, py = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <=nx < row and 0 <=ny < col and grid[nx][ny] == c:
                        if (nx, ny) in visited:
                            if (nx, ny) != (px, py):
                                return True
                        else:
                            q.append((nx, ny, x, y))
                            visited.add((nx, ny))
            return False

        visited = set()        
        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and bfs(r, c , grid[r][c]):
                    return True
        return False