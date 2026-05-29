class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        itoc = {}
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in itoc:
                return [itoc.get(comp), i + 1]
            itoc[n] = i + 1