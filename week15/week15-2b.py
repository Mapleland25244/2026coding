# week15-2b.py 學習計畫 DP - Mutidimensional 第2題
# LeetCode 1143. Longest Common Subsequence bottom-up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N) for i in range(M)]
        
        for i in range(M):
            for j in range(N):
                # case1 = dp[i-1][j] 看上面
                # case2 = dp[i][j-1] 看左邊
                # case3 = dp[i-1][j-1] + 1 看左上角(如果相同，看左上角 + 1)
                if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j])
        return dp[M-1][N-1]