# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        if "".join(sorted(s)) == "".join(sorted(t)):
            return True
        else:
            return False

## main
if __name__ =="__main__":
    s = "anagram"
    t = "aaangrm"

    Sol = Solution()
    print(Sol.isAnagram(s,t))
