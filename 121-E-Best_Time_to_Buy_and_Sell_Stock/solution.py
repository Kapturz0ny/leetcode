from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = prices[0], prices[0]

        for price in prices:
            if price > sell:
                sell = price
                max_profit = max(max_profit, sell - buy)
            if price < buy:
                buy = price
                sell = price

        return max_profit
