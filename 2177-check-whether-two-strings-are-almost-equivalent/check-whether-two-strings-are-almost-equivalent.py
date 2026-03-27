class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cFreqword1, cFreqword2  =  Counter(word1), Counter(word2)
        for char in cFreqword1 | cFreqword2:
            if abs(cFreqword1[char] - cFreqword2[char]) > 3:
                return False
        return True
