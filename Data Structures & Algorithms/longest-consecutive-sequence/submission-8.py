class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        mins = []
        unique = set(nums)
        for n in nums:
            if n-1 not in unique:
                mins.append(n)
        
        counts = [1] * len(mins)
        for i, m in enumerate(mins):
            j = m
            while j+1 in unique:
                j += 1
                counts[i] += 1
        
        return max(counts)


"""
nums=[4,7,1,3,-1,0,9,5,8,-1,6 -8]

-1, 3, -8

[3, 9, 1]
"""