# 435. Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# the key is to sort the intervals and then check overlaps
# if there's an overlap, maintain the interval on the left side and erase the right one
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or interval[0] >= merged[-1][1]:
                merged.append(interval)
            # if there's overlap, maintain the interval with smaller right boundary
            elif interval[1] < merged[-1][1]:
                merged[-1] = interval
        
        return len(intervals) - len(merged)

## main
if __name__ =="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))