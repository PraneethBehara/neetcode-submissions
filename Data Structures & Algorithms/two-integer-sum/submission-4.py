class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxMap = {}
        for i, n in enumerate(nums):
            diff = target - n  
            if diff in indxMap:
                return [indxMap[diff], i]
            indxMap[n] = i
                     