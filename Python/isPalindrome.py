# 125. Valid Palindrome
# Given a string s, return true if it is a palindrome, or false otherwise.
# the input can contain non-alphanumeric chars
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        if s == "":
            return True
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        
        if i == j:
            if s[i] == s[j]:
                return True
            else:
                return False
        if i > j:
            return True

## main
if __name__ =="__main__":
    s = "abaa ba"
    Sol = Solution()
    print(Sol.isPalindrome(s))

    