# 90. Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

class Solution:
    def subsetsWithDup(self, nums):
        result=[]
        nums.sort()#To handle duplicate first we sort the array ( adjacent elements will be similar )
        def backtrack(nums,index=0,arr=[]):
            result.append( arr[:] )
            for i in range( index, len(nums)):
                if i != index and nums[i] ==nums[i-1]: #skip the duplicates, except for the first time
                    continue
                arr.append(nums[i]) #include the element
                backtrack(nums,i+1,arr ) #explore
                arr.pop() #remove the element
            
        backtrack(nums)
        return result

## main
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.subsetsWithDup([1,2,2]))    