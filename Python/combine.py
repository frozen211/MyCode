# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

class Solution(object):
    def combine(self, n, k):   
        sol=[]
        def backtrack(remain,comb,nex):
            # solution found
            if remain==0:
                # python doesn't create new object when you append
                # so append comb will be wrong
                sol.append(comb[:])
            else:
                # iterate through all possible candidates
                for i in range(nex,n+1):
                    # add candidate
                    comb.append(i)
                    #backtrack
                    backtrack(remain-1,comb,i+1)
                    # remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol

## main
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.combine(4,2))
