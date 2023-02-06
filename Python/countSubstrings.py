# 647. Palindromic Substrings
# Given a string s, return the number of palindromic substrings in it.
# the key is to assume each element as the "center" and expand from it
class Solution:
    def countSubstrings(self, s):
        count = 0
        
        for i in range(len(s)):
            # odd palidromes
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # even palidromes
            l,r = i,i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        return count

## main
if __name__ =="__main__":
    s = "aaa"
    sol = Solution()
    print(sol.countSubstrings(s))