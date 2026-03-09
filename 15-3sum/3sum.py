class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return res
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                r = len(nums) - 1
                while l < r:
                    target = nums[i] + nums[l] + nums[r]
                    if target > 0:
                        r -= 1
                    elif target < 0:
                        l += 1
                    else:                  
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums [l]:
                            l += 1                                          
        return res
