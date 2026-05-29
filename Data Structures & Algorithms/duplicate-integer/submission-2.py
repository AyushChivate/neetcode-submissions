import collections

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        nums_list = list(nums_set)
        return collections.Counter(nums_list) != collections.Counter(nums)

         
