class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n  = len(grid[0])
        def bfs(i, j , c):
            visited.add((i, j))
            q = deque([(i, j, -1, -1)])
            while(q):
                x, y, px, py = q.popleft()
                for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==c:
                        if (nx, ny) in visited:
                            if (nx, ny)!=(px, py):
                                return True
                        else:
                            q.append((nx,ny,x,y))
                            visited.add((nx,ny))
            return False

        visited = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and bfs(i, j, grid[i][j]):
                    return True
        return False