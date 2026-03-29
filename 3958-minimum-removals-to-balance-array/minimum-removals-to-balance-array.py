class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        max_winsize = 1         
        for right in range(n):
            while nums[right] > nums[left] * k:
                left += 1
            max_winsize = max(max_winsize, right - left + 1)        
        return n - max_winsize

            
