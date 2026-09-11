
'''
// [1, 2, 3, 4, 5]
if mid > left and mid < right:
    regular binary search

// [3, 4, 5, 1, 2]
// [3, 4, 5, 6, 7, 1, 2]
if mid > left and mid > right:
    if target <= mid and target > right:
        go left
    else:
        go right

// [5, 1, 2, 3, 4]
// [6, 7, 1, 2, 3, 4, 5]
if mid < left and mid < right:
    if target >= mid and target < left:
        go right
    else:
        go left


6, 7, 1, 2, 3, 4, 5

3, 4, 5, 6, 7, 1, 2

5, 1, 2, 3, 4

3, 4, 5, 1, 2

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_i, right_i = 0, len(nums) - 1

        while left_i <= right_i:
            mid_i = (left_i + right_i) // 2

            left, mid, right = nums[left_i], nums[mid_i], nums[right_i]
            
            if target == mid:
                return mid_i

            if mid >= left and mid <= right:
                if target < mid:
                    right_i = mid_i - 1
                else:
                    left_i = mid_i + 1
            elif mid >= left and mid >= right:
                if target < mid and target > right:
                    right_i = mid_i - 1
                else:
                    left_i = mid_i + 1
            elif mid <= left and mid <= right:
                if target > mid and target < left:
                    left_i = mid_i + 1
                else:
                    right_i = mid_i - 1
            else:
                return -1
        
        return -1