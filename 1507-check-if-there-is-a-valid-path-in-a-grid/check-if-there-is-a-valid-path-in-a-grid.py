class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        U, D, L, R = (-1, 0), (1,0), (0, -1), (0,1)        
        ROW, COL = len(grid), len(grid[0])        
        hmap = {1: {L:L, R:R}, 2: {U:U, D:D}, 3: {R:D, U:L}, 4: {L:D, U:R}, 5:{R:U, D:L}, 6:{D:R, L:U}}        
        
        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        
        while q:
            r, c = q.popleft()            
            if r == ROW-1 and c == COL-1:
                return True                        
            for dr, dc in hmap[grid[r][c]].values():
                nr, nc = r + dr, c + dc                
                if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited and (dr,dc) in hmap[grid[nr][nc]]:
                    q.append((nr, nc)) 
                    visited.add((nr, nc))        
        return False