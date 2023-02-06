# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# the key is to traverse backward
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last=m+n-1
        #index of the element
        while(m>0 and n>0):
            if(nums1[m-1]>nums2[n-1]):
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1
        while(n>0):
            nums1[last]=nums2[n-1]
            n-=1
            last-=1

## main
if __name__ =="__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)
                