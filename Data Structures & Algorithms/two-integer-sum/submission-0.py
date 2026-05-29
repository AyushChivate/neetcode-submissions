class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = []
        for i, num in enumerate(nums):
            if num in complements:
                return [complements.index(num), i]
            complements.append(target - num)
