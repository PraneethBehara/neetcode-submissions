class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indxMap: dict[int, int] = {}
        for i, n in enumerate(nums):
            diff = target - n  
            if diff in indxMap and indxMap[diff] != i:
                return [indxMap[diff], i]
            indxMap[n] = i
                     