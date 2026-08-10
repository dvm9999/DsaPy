class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, n = [], len(candidates)
        def dfs(i, path, ctarget):
            if ctarget == 0:
                res.append(path[:])
                return 
            if i >= n or candidates[i] > ctarget:
                return
            path.append(candidates[i])
            dfs(i, path, ctarget - candidates[i])
            path.pop()
            dfs(i + 1, path, ctarget)
        candidates.sort()
        dfs(0, [], target)
        return res
                
            