class Solution:
    def threeSum(self, nums_i: List[int]) -> List[List[int]]:
        outer = []
        nums = sorted(nums_i)
        for n in range(len(nums)):
            inner = []
            i, j = n + 1, len(nums) - 1
            while i < j:
                if n > 0 and nums[n] == nums[n-1]:
                    break
                if nums[i] + nums[j] == -nums[n]:
                    inner.append([nums[n], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif nums[i] + nums[j] < -nums[n]:
                    i += 1
                else:
                    j -= 1
            if len(inner) > 0:
                outer.extend(inner)

        return outer

"""
[-4, -1, -1, 0, 1, 2]

[-8, -5, -4, -1, 0, 2, 4, 5, 7, 9]

[
    [-8, -1, 9],
    [-5, -4, 9],
    [-5, 0, 5],
    [-4, 0, 4],
    [-4, -1, 5]
]
"""