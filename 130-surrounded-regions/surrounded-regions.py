class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col  = len(board), len(board[0]) 
        def dfs(i, j): 
            board[i][j] = "V"           
            for a, b in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)] :
                if 0 <= a < row and 0 <= b < col and board[a][b] == "O":
                    dfs(a,b)
        for r  in range(row):
           for c in range(col):
                if board[r][c] == 'O' and (r in [0, row - 1] or c in [0, col - 1]):
                    dfs(r, c)
        for r in range( row):
            for c in range(col): 
                board[r][c] = "O" if board[r][c] == "V" else "X"
        
                
        