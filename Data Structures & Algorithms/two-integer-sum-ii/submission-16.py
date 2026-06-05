class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left, right = 0, length - 1

        while left <= right and left >= 0 and right <= length - 1 :
            summ = numbers[left] + numbers[right]

            if summ == target:
                return [left + 1, right + 1]
            
            if summ < target:
                left += 1
                continue
            
            if summ > target:
                right -= 1
                continue
        return []



"""
[5,6,7,8,10]
15

[-10, -4, 1, 1, 2, 2, 3, 4, 7, 9, 11, 24] 10

1. start two pointers in the middle
2. right keeps increasing until it overshoots
3. once it overshoots, bring it back 1 and reduce left by 1
4. repeat steps 2 and 3.

"""