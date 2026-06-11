class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_product = 0

        while left < right:
            minimum = min(heights[left], heights[right])
            distance = right - left
            product = minimum * distance
            if product > max_product:
                max_product = product
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
        return max_product