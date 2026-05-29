class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(max(freq.values()) + 1)]
        for num, f in freq.items():
            buckets[f].append(num)
        
        o = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                o.append(j)
                if len(o) == k:
                    return o