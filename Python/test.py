
class Solution:
    def __init__(self):
        self.val = 1
        
    def adding(self,num):
        return num + self.val


## main
if __name__ =="__main__":
    nums = 5
    sol = Solution()
    ans = sol.adding(nums)
    print(ans)
    print(nums)