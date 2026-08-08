class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid, right = 0, len(nums) // 2, len(nums) - 1

        while left <= right:
            if nums[mid] == target:
                return mid
            
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

            mid = (right + left) // 2
        return -1
        