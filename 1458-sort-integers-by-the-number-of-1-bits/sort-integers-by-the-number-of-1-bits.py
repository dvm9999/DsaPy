class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        setBitCount = defaultdict(list)
        for i, num in enumerate(arr):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            setBitCount[count].append(arr[i])
        ans = [] 
        for k in sorted(setBitCount):
            ans.extend(sorted(setBitCount[k]))
        return ans
