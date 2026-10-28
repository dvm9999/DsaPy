# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:  
    def serialize(self, root):
        q  = deque([root]) 
        res = [] 
        while q:
            for _ in range(len(q)):
                curr = q.popleft() 
                if not curr:
                    res.append("#")
                    continue
                res.append(str(curr.val)) 
                q.append(curr.left)
                q.append(curr.right)     
        while res  and  res[-1] == "#":
            res.pop()
        return ",".join(res)
    def deserialize(self, data):
        if not data: return None
        datalst = data.split(",")[::-1]            
        root  =  TreeNode(int(datalst.pop())) 
        q = deque([root]) 
        while datalst:
            curr = q.popleft()            
            if not curr: 
                continue             
            currnode0 = datalst.pop()                 
            if not curr.left: 
                if currnode0 != "#":
                    curr.left  =  TreeNode(int(currnode0)) 
                    q.append(curr.left)  
            if not datalst:
                break
            currnode2 = datalst.pop()
            if not curr.right:                
                if currnode2 != "#":
                    curr.right = TreeNode(int(currnode2)) 
                    q.append(curr.right)                    
        return root 

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))