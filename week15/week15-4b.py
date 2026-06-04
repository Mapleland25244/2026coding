# week15-4b.py 學習計畫 DP - Multidimensional 第4題
# LeetCode 72. Edit Distance 編輯(插入1字母、刪掉1字母、換掉1字母)幾次後，會得到 word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2) # 兩字串的長度
        dp = [[0] * (N+1) for i in range(M+1)]
        for i in range(M+1): dp[i][0] = i
        for j in range(N+1): dp[0][j] = j
        for i in range(M):
            for j in range(N):
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1
                if word1[i] == word2[j]: dp[i+1][j+1] = dp[i][j]
        return dp[M][N]

