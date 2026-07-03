class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_ids = {}
        for each in nums:
            if each in unique_ids:
                print(each)
                return True
            else:
                unique_ids[each] = 1

        return False