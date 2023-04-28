# 33. Search in Rotated Sorted Array
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k = nums.index(max(nums)) + 1
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R)//2
            M1 = (M + k) % len(nums)
            
            if nums[M1] > target:
                R = M - 1
            if nums[M1] < target:
                L = M + 1
            if nums[M1] == target:
                return M1
        return -1

## main
if __name__ =="__main__":
    s = [4,5,6,7,0,1,2]

    Sol = Solution()
    print(Sol.search(s,1))