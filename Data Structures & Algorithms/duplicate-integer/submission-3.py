class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for each in nums:
            if each in nums_set:
                return True
            else:
                nums_set.add(each)
        
        return False
