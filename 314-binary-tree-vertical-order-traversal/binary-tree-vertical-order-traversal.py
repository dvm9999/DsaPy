# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 0)])
        d = defaultdict(list)
        res = []
        while queue:
            curr, y =  queue.popleft()
            d[y].append(curr.val)
            if curr.left:
                queue.append((curr.left, y - 1))
            if curr.right:
                queue.append((curr.right, y + 1))       
        for k in sorted(d):
            res.append(d[k])
        return res