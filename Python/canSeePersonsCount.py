# 1944. Number of Visible People in a Queue

# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
# You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
# A person can see another person to their right in the queue if everybody in between is shorter than both of them. 
# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

# monotonic stack is used but I still can't make sense of it
class Solution(object):
    def canSeePersonsCount(self, heights):
        answer = len(heights)*[0]
        stack = []
        for i in range(len(heights)-1,-1,-1):
            count = 0
            while stack and heights[i] > heights[stack[-1]]:
                count += 1
                # a tall person will shadow the short person on his right
                # the shorter person will no longer be visible
                stack.pop()
            # the current person can see the next taller person to his right
            if stack:
                count += 1
            
            stack.append(i)
            answer[i] = count

        return answer

## main
if __name__ =="__main__":
    nums = [10,6,8,5,11,9]
    sol = Solution()
    print(sol.canSeePersonsCount(nums))
                