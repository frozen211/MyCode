# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. Return the answer in any order.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        D = {}
        D[2] = ["a","b","c"]
        D[3] = ["d","e","f"]
        D[4] = ["g","h","i"]
        D[5] = ["j","k","l"]
        D[6] = ["m","n","o"]
        D[7] = ["p","q","r","s"]
        D[8] = ["t","u","v"]
        D[9] = ["w","x","y","z"]

        def generate(lst):
            if len(lst) == 1:
                return D[int(lst[0])]
            res = []
            fst = int(lst[0])
            for i in range(len(D[fst])):
                letter = D[fst][i]
                res += (letter + p for p in generate(lst[1:]))
            return res
        
        Res = generate(digits)
        return Res

## main
if __name__ == "__main__":
    Sol = Solution()
    print(Sol.letterCombinations("23"))   

