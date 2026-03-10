class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and stack[-1] + c in ["()", "{}", "[]"]:
                stack.pop()
            else:
                return False          
        return not stack