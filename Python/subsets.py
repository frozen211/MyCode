# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).

class Solution(object):
    # # my solution has high runtime
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     if nums == []:
    #         return [[]]
        
    #     D = {}
    #     def generate(ns):
    #         if ns == []:
    #             return []
    #         if tuple(ns) not in D:
    #             D[tuple(ns)] = 1    
    #             res = [ns]
    #         else:
    #             res = []
    #         for i in range(len(ns)):
    #             temp = generate(ns[:i]+ns[i+1:])
    #             res = res + temp
    #         return res
        
    #     Res = generate(nums) + [[]]

    #     return Res

    # use backtracking
    def subsets(self, nums):
        self.ans = []
        self.length = len(nums)
        self.helper([],nums,0)
        return self.ans

    def helper(self,arr,nums,ind):
        if ind < self.length:
            for i in range(ind,self.length):
                self.helper(arr+[nums[i]],nums,i+1)
        self.ans.append(arr)

## main
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.subsets([1,2,3]))    
        
