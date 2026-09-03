class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
            [[1,2,4,8],
            [10,11,12,13],
            [14,20,30,40],
            [50,60,70,80],
            [90,100,101,102],
            [103,104,105,106]]
        """

        left, right = 0, len(matrix) - 1
        middle = (left + right) // 2

        while (left <= right):
            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][-1]:
                left = middle + 1
            else:
                break
            middle = (left + right) // 2
        

        l, r = 0, len(matrix[middle]) - 1
        m = (l + r) // 2

        while (l <= r):
            if target < matrix[middle][m]:
                r = m - 1
            elif target > matrix[middle][m]:
                l = m + 1
            else:
                return True
            m = (l + r) // 2
        
        return False

            

        