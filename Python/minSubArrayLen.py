# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# the key is not to use sum(), which costs too much time
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        L = len(nums)+1
        lp = 0
        rp = 0
        S = 0
        while rp < len(nums):
            S  = S + nums[rp]
            l += 1
            if S < target:
                # move right pointer
                rp += 1
            else:
                while S - nums[lp] >= target:
                    # move left pointer
                    S = S - nums[lp]
                    lp += 1
                    l -= 1
                # store the smallest size
                if l < L:
                    L = l
                rp += 1

        if L == len(nums)+1:
            return 0
        else:
            return L


## main
if __name__ =="__main__":
    nums = [5,1,3,5,10,7,4,9,2,8]
    target = 155
    sol = Solution()
    print(sol.minSubArrayLen(target,nums))
    