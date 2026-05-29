class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_products = self.calculateRightOrLeftProducts(nums)
        list.reverse(nums)
        left_products = self.calculateRightOrLeftProducts(nums)
        list.reverse(left_products)

        print(right_products)
        print(left_products)

        return [l * r for l, r in zip(left_products, right_products)]

    
    def calculateRightOrLeftProducts(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        for i in range(1, len(nums)):
            products[i] = nums[i-1] * products[i-1]
        return products



