# generate all permutations of string s in a recursive way
# T(s) = sum(s[i] + T(s[:i]+s[i+1:]))
# if len(s)==1, then return s
def generatePermutation(s):
    if len(s) == 1:
        return s
    
    res = []
    for i in range(len(s)):
        res += (s[i] + p for p in generatePermutation(s[:i]+s[i+1:]))
    
    return res

s = "abc"
Res = generatePermutation(s)
print(Res)
