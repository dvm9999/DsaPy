# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node, par):
            if not node: return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        queue = deque([target])
        visited = {target}
        while queue and k:            
            for _ in range(len(queue)):
                curr = queue.popleft()
                for nei in [curr.left, curr.right, parent[curr]]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            k -= 1
        res = []
        while queue:
            res.append(queue.popleft().val)
        return res
        