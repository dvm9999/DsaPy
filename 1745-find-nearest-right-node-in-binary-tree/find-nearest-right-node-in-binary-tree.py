# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if not root : return None
        queue = deque([root, None]) 
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr: continue             
                if curr == u:
                    return queue[0]              
                if curr.left :
                    queue.append(curr.left)
                if curr.right :
                    queue.append(curr.right)
            queue.append(None)
        return None                               
        