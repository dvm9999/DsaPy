class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = [] 
        diff = float('inf')
        closest = None
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total == target: return target
                    if abs(total - target) < diff:
                        diff = abs(total - target)
                        closest = total
                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1                                                         
        return closest