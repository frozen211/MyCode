# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.
class Solution:
    def longestPalindrome(self, s):
        ans=''
        for i in range(len(s)):
            ans=max(ans,expand(s,i,i), expand(s,i,i+1), key=len)
        return ans
            
def expand(s,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j]

## main
if __name__ =="__main__":
    s = "babad"

    Sol = Solution()
    print(Sol.longestPalindrome(s))