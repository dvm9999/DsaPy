class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writeidx = 0
        for readidx in range(len(nums)):
            if nums[readidx] != val:
                nums[writeidx] = nums[readidx] # new data, to write 
                writeidx = writeidx + 1
        return writeidx
