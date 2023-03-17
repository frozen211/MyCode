# 41. First Missing Positive
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is not a constant space solution but it is simple
        unique = set(nums)
        i = 1
        while i in unique:
            i += 1
        return i

## main
if __name__ =="__main__":
    nums = [-11,-1,0,30,40]
    sol = Solution()
    print(sol.firstMissingPositive(nums))