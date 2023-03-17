# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        # here's the simplest solution
        # unique = set(nums)
        # if len(unique) != len(nums):
        #     return True
        # else:
        #     return False

        # here's a normal solution
        if len(nums) == 1:
            return False
        temp = sorted(nums)
        for i in range(len(temp)-1):
            if temp[i] == temp[i+1]:
                return True
        return False


## main
if __name__ =="__main__":
    nums = [2,3,4,2]
    sol = Solution()
    print(sol.containsDuplicate(nums))