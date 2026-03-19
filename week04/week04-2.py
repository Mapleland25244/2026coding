# week04-2.py 學習計畫 Prefix Sum 第一題
# LeetCode 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain) # 陣列的長度 N
        H = 0 # 一開始的高度是 0
        ans = 0 # 答案是0因為一開始高度是0
        for i in range(N): # 逐個加起來
            H += gain[i] # 現在增減的量 gain[i] 加進 H
            ans = max(ans, H) # 更新最高答案
        return ans
