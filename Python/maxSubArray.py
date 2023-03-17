# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# The key idea is: if adding an element makes the currSumSubarray negative, then it means we should 
# start a new subarray. Thus, we set the currSumSubarray to be 0.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maximumSum, currSumSubarray = float('-inf'), 0
        for i in range(n):
            currSumSubarray += nums[i]
            maximumSum = max(maximumSum, currSumSubarray)
            currSumSubarray = max(currSumSubarray, 0)
        return maximumSum

## main
if __name__ =="__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.maxSubArray(nums))