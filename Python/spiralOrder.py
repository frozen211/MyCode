# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

# There is no secret, just plainly follow the spiral order and print the elements out
class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0) # 1

            if matrix and matrix[0]: # 2 
                for line in matrix:
                    result.append(line.pop())

            if matrix: # 3
                result += matrix.pop()[::-1]

            if matrix and matrix[0]: # 4
                for line in matrix[::-1]:
                    result.append(line.pop(0))
        return result

## main
if __name__ =="__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    for row in matrix:
        print(row)
    print()
    Sol = Solution()
    R = Sol.spiralOrder(matrix)
    print(R)