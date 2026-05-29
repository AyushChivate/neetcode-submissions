class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = self.calc_half(nums)
        left = self.calc_half(nums[::-1])

        products = []

        for r, l in zip(right, reversed(left)):
            products.append(r*l)


        return products
    
    def calc_half(self, nums: List[int]) -> List[int]:
        half = [1]
        total = 1
        for num in nums[0:-1]:
            total *= num
            half.append(total)
        return half



"""
1, 1, 2, 8,
48, 24, 6, 1

48, 48, 

1, 6, 24, 48, 48


[2, 2, 4, 5, 3]

[1, 2, 4, 16, 80]
[1, 3, 15, 60, 120]

left =  [1, 2, 4, 16, 80]
right = [120, 60, 15, 3, 1]

[120, 120, 60, 48, 80]

"""