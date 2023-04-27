# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == "":
            return [[""]]

        D = {}
        for s in strs:
            # generate unique key
            mask = [0]*26
            for j in s:
                mask[ord(j) - ord('a')] += 1
            mask1 = ""
            for j in mask:
                mask1 = mask1 + str(j) + " "
            # put in the dictionary
            if mask1 not in D.keys():
                D[mask1] = []
                D[mask1].append(s)
            else:
                D[mask1].append(s)
        # output
        Res = []
        for i in D.keys():
            Res.append(D[i])
        
        return Res

## main
if __name__ =="__main__":
    strs = ["ddddddddddg","dgggggggggg"]

    Sol = Solution()
    print(Sol.groupAnagrams(strs))