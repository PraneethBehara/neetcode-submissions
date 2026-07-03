class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums: Set[int] = set(nums)

        return len(unique_nums) != len(nums)

