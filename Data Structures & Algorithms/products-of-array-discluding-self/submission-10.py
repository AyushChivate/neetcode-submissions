class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        prefix, suffix = 1, 1

        for i, _ in enumerate(nums):
            j = len(nums) - i - 1

            sol[i] *= prefix
            sol[j] *= suffix

            prefix *= nums[i]
            suffix *= nums[j]
 
        return sol


        