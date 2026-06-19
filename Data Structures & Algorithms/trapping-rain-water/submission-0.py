class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        l_max, r_max = heights[left], heights[right]
        running_total = 0

        while left < right:
            # set the left and right maxes
            l_max = max(l_max, heights[left])
            r_max = max(r_max, heights[right])
            # get the minimum max
            min_max = min(l_max, r_max)

            # subtract left and right values from min max
            l_sum, r_sum = min_max - heights[left], min_max - heights[right]

            # update the running total
            running_total += max(0, l_sum)
            running_total += max(0, r_sum)

            # figure out which pointer to move
            if heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        
        return running_total





"""
two pointers, start at start and end
find maxes so far

maxL: 0, 2, 2, 2, 3, 3, 3, 3
maxR: 1, 1, 2, 2, 3, 3, 3, 3

L: 0, 2, 2, 0, 3, 3, 1, 0, 1, 3
R: 1, 1, 2, 2, 2, 3, 3, 3, 3, 3

sum = 2 + 2 + 3 + 2

"""