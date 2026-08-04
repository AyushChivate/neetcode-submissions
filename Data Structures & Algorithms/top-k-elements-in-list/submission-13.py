class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num] += 1
        
        freq_to_nums = [[] for _ in range(max(num_to_freq.values()) + 1)]
        for num, freq in num_to_freq.items():
            freq_to_nums[freq].append(num)
        
        sol = []
        for nums in reversed(freq_to_nums):
            if k <= 0:
                break
            sol.extend(nums)
            k -= len(nums)

        return sol


"""
[0, 1, 3, 1, 9, 2, 9, 2, 0, 1]

0: 2
1: 3
3: 1
9: 2
2: 2


[
  0: []
  1: [3]
  2: [0, 9, 2],
  3: [1]
]
"""