class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        readidx, writeidx = 0, 0
        for readidx in range(len(nums)):
            if nums[readidx] != nums[writeidx]:
                writeidx += 1
                nums[writeidx] = nums[readidx]
        return  writeidx + 1