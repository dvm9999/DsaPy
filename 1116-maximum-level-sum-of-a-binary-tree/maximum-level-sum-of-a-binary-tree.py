# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxl  = 1
        currSum = root.val
        queue = deque([root])
        l = 1        
        while queue:
            s = 0             
            for _ in range(len(queue)):
                curr = queue.popleft()
                s += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if s > currSum:
                maxl= l
                currSum = s
            l += 1
        return  maxl