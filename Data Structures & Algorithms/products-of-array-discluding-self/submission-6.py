class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_products = self.calculateRightOrLeftProducts(nums)
        left_products = self.calculateRightOrLeftProducts(nums[::-1])[::-1]

        print(right_products)
        print(left_products)

        return [l * r for l, r in zip(left_products, right_products)]

    
    def calculateRightOrLeftProducts(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        for i in range(len(nums)):
            running_product = 1
            for j in range(i+1, len(nums)):
                running_product *= nums[j]
            products[i] = running_product
        return products



