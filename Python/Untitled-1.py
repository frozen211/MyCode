# 76. Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# This code will not pass all test cases, for example, s="aa" and t="aa". The expected return is "aa" instead of "a"
# I put it at here because it is an example of checking if all characters in t is also in s
# it also uses sort() and customizes the criteria for sorting.

class Solution(object):
    def minWindow(self, s, t):
        if s == "":
            return ""
        if len(s) < len(t):
            return ""

        l = 0
        r = 0
        L = len(s)+2
        W = []
        while r < len(s):
            r += 1
            if self.ContainsAll(s[l:r],t):
                L = len(s[l:r])
                # check if the window can be shorter
                while self.ContainsAll(s[l+1:r],t):
                    l += 1
                    L = len(s[l:r])
                # store the window
                W.append(s[l:r])

        if L == len(s)+2:
            return ""
        else:
            # return the shortest window
            W.sort(key=len)
            return W[0]
    
    def ContainsAll(self, s, t):
        # the helper function to check if all chars are in s
        return 0 not in [c in s for c in t]


## main
if __name__ =="__main__":
    s = "aa"
    t = "aa"
    sol = Solution()
    print(sol.minWindow(s,t))