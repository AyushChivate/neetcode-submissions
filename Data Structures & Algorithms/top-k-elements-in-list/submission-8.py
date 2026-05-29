class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = defaultdict(int)
        for num in nums:
            f_map[num] += 1
        print(f_map)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in f_map.items():
            buckets[freq].append(num)
        print(buckets)
        
        res = []
        for bucket in reversed(buckets):
            for num in bucket:
                if len(res) == k:
                    return res
                res.append(num)

        return res
