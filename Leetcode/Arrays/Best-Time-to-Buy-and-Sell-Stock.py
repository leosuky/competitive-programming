"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
------------------------------------------------------------------------------------
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set our initial profit to 0
        profit = 0

        # set the lowest price to 0
        anchor = 0

        # Iterate through the list of prices
        for i in range(len(prices)):
            # current profit = current price minus lowest price
            value = prices[i] - prices[anchor]

            # if current price is less than lowest price
            if prices[i] < prices[anchor]:
                # replace the lowest price with current price
                anchor = i
            # if current profit is greater than initial profit
            if value > profit:
                # replace initial profit with current profit
                profit = value


        return profit


"""
The algorithm above has a time complexity of 0(n)
and a space complexity of 0(1)
----------------------------------------------
ARRAY --- EASY
"""
