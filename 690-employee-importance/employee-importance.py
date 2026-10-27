"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:   
        idmap, ans = {}, 0
        for i, emp in enumerate(employees):
            idmap[emp.id] = i
        def dfs(id):
            nonlocal ans
            indx = idmap[id]
            ans += employees[indx].importance
            for subid in employees[indx].subordinates:
                dfs(subid)
        dfs(id)
        return ans 