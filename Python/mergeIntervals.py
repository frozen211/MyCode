# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# sort the intervals and then merge them
class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    
## main
if __name__ =="__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(intervals))
