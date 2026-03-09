class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, subset = [], []        
        def kSum(k, start, target):
            # Base case for k=2, use two-pointer approach
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append(subset + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return
            
            # Recursive case for k > 2
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                subset.pop()
        kSum(4, 0, target)
        return res