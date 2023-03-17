# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
import copy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]*len(nums)
        right = [1]*len(nums)
        # compute the product to the left
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        # compute the product to the right
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        # generate the answer
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = left[i]*right[i]
        
        return ans

## main
if __name__ =="__main__":
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))