class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_id_set = set()
        for each in nums:
            if each in unique_id_set:
                return True
            else:
                unique_id_set.add(each)

        return False