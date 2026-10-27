# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        parent = { }        
        def dfs(node, par) :
            nonlocal target
            if node :
                if node.val == k :
                    target = node
                parent[node] = par 
                dfs(node.left, node)
                dfs(node.right , node) 
        target  = None
        dfs(root, None)        
        queue = deque([target])       
        visited = {target}
        while queue:
            curr =  queue.popleft() 
            if not curr.left and not curr.right :
                return curr.val 
            for nei in  [parent[curr], curr.left, curr.right] :
                if  nei and nei not in visited:
                    visited.add(nei)
                    queue.append(nei) 
        return None
       
            
