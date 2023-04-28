# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        R = len(nums) - 1
        L = 0

        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            if nums[M] > target:
                R = M - 1
            elif nums[M] < target:
                L = M + 1
        
        return -1

## main
if __name__ =="__main__":
    s = [-1,0,3,5,9,12]

    Sol = Solution()
    print(Sol.search(s,-99))