# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
import heapq
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the easiest way is heapify, which has a runtime of O(logn)
        # binary search will also do the trick
        heapq.heapify(nums)
        return nums[0]

## main
if __name__ =="__main__":
    s = [3,4,5,1,2]

    Sol = Solution()
    print(Sol.findMin(s))
