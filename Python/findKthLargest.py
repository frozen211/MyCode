# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heap will be the easiest way, but the runtime may not be O(n)
        heapq.heapify(nums)
        # exract the k largest values and store them in non-decreasing order
        L = heapq.nlargest(k,nums)
        return L[-1]

        

## main
if __name__ =="__main__":
    s = [3,2,3,1,2,4,5,5,6]

    Sol = Solution()
    print(Sol.findKthLargest(s,4))