class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt( path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            cand = []
            for n in nums:
                if n not in path:
                    cand.append(n)
            for c in cand:
                path.append(c)
                bt(path)
                path.pop()
        bt([])
        return res
