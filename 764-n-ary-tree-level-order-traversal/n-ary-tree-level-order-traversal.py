"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        ans = [] 
        while queue:
            ans.append([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                ans[-1].append(curr.val)
                for child in curr.children:
                    queue.append(child)
        return  ans