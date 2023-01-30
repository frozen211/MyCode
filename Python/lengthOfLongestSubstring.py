# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        
        l = 0
        L = 0 
        lp = 0
        rp = 0
        subs = ""
        while rp < len(s):
            if s[rp] not in subs:
                subs += s[rp]
                rp += 1
                l += 1
                if l >= L:
                    L = l
            else:
                # once detect a repeated char, remove elements in subs until no duplicate
                subs += s[rp]
                lp = subs.find(s[rp])
                subs = subs[lp + 1:]
                l = len(subs)
                rp += 1

        return L


## main
if __name__ =="__main__":
    S = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(S))