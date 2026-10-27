# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:    
        if not root: return []
        queue = deque([root])
        res = []
        while queue:
            res.append([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                res[-1].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not len(res) % 2 :
                res[-1] = res[-1][::-1]
        return res