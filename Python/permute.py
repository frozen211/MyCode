# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        
        Res = []
        for i in range(len(nums)):
            Res += ([nums[i]] + p for p in self.permute(nums[:i]+nums[i+1:]))


        return Res

## main
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.permute([1,2,3]))

