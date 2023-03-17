# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = 99999
        for i in range(len(prices)):
            # keep track of the min price
            if prices[i] < min_price:
                min_price = prices[i]
            # update the max profit
            if prices[i] - min_price >= profit:
                profit = prices[i] - min_price
        return profit

## main
if __name__ =="__main__":
    nums = [7,6,5,4,3]
    sol = Solution()
    print(sol.maxProfit(nums))

