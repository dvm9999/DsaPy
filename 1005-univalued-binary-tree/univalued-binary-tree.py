# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if (root.left and  root.val !=  root.left.val) or (root.right and root.right.val != root.val):
            return False
        return (self.isUnivalTree(root.left) and self.isUnivalTree(root.right))