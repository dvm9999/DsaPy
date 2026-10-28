"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root):
        if not root: return 0 
        if not root.children: return 1
        height = [self.maxDepth(ch) for ch in root.children]
        return max(height) + 1 
            
        
        