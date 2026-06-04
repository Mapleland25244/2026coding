# week15-3.py 學習計畫 DP - Mutidimensional 第3題
# LeetCode 714. Best Time to Buy and Sell Stock with Transaction Fee
from functools import *
class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        @cache
        def helper(i, status): # 現在考慮 prices[i] 手上是否有股票的狀態 status
            if i>=len(prices): return 0 # 終止條件
            # 手上有股票，可以考慮「要不要賣」 賣的時候要付手續費 fee
            if status:
                profits = prices[i] + helper(i+1, 0) - fee # 得到錢 prices[i]
                keep = helper(i+1, 1) # 不買不賣
                return max(profits, keep)
            # 手上沒有股票，可以考慮「要不要買」
            else:
                cost = -prices[i] + helper(i+1, 1) # 花了錢 prices[i] 得到股票
                keep = helper(i+1, 0) # 不買不賣
                return max(cost, keep)
        return helper(0, 0) # 從第0天開始思考，手上沒有股票