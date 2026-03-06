class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows <= 1: return s
        rowstr = [''] * numRows
        index, step = 0, 1
        for c in s:
            rowstr[index] += c
            if index == 0:
                step = 1                       
            if index == numRows - 1:
                step = - 1
            index += step
        return "".join(rowstr)
    # index control to make a cycle of writes , but read is linear over s.