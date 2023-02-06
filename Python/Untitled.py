# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# The solution is a typical insertion sort
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >=0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        
## main
if __name__ =="__main__":
    nums = [2,0,1]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)