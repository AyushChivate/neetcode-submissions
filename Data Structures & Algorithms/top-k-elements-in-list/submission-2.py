class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fm = {}
        for n in nums:
            if n not in fm:
                fm[n] = 0
            fm[n] += 1

        output = []
        for n in range(k):
            maxVal = 0
            maxKey = 0
            for key in fm:
                if fm[key] > maxVal:
                    maxVal = fm[key]
                    maxKey = key
            output.append(maxKey)
            fm.pop(maxKey)
        return output