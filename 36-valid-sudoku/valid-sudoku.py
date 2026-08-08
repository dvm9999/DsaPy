class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set) 
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                v  = board[r][c] 
                if v  == "." :
                    continue
                bno = (r // 3) * 3 + c // 3  
                if v in row[r] or v in col[c]  or v in box[bno]:
                    return False
                row[r].add(v)
                col[c].add(v)
                box[bno].add(v)
        return True