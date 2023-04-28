# 74. Search a 2D Matrix
"""
You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
"""
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            # here's how to locate the value of the mid point
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

## main
if __name__ =="__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

    Sol = Solution()
    print(Sol.searchMatrix(matrix,3))