import collections

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return collections.Counter(list(set(nums))) != collections.Counter(nums)

         
