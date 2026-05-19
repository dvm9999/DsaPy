class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        if not nums: return [-1, -1]
        def search(x):
            lo, hi = 0, len(nums) - 1           
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid - 1                    
            return lo        
        lo = search(target)
        hi = search(target + 1) - 1        
        return [lo, hi] if lo <= hi else [-1, -1]
        
       
       