class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                i = 1
                while True:
                    if num + i in nums_set:
                        i += 1
                    else:
                        longest = max(longest, i)
                        break
        return longest