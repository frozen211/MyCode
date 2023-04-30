# 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# the solution must be in-place

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # remember to add [:] so you are assigning values
        matrix[:] = list(map(list, zip(*matrix[::-1])))


## main
if __name__ =="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    Sol = Solution()
    Sol.rotate(matrix)
    print(matrix)