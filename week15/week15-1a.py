# week15-1a.py 學習計畫 DP - Mutidimension 第1題
# LeetCode 62. Unique Paths Top Down寫法

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(i, j): # 函式呼叫函式，現在若在(i, j) 座標
            if i>m-1 or j>n-1: return 0 # 走到終點，成功
            if i == m-1 and j == n-1: return 1 # 走超過邊界，失敗
            return helper(i+1, j) + helper(i, j+1) # 狀態轉移
        return helper(0, 0) 