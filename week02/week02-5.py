# week02-5.py 學習計畫 Two Pointers 第4題 Medium 題
# LeetCode 1679. Max Number of K-Sum Pairs
# 希望找到「加起來 == k」的 pair 兩兩一組，共幾組
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort() # 小到大排好，等一下「左邊挑一個、右邊挑一個」看看能不能組合
        i, j = 0, len(nums)-1 # 最左邊 i 對應最小，最右邊j 對應
        while i < j: # 還沒有撞在一起，就可以左右個挑一個
            sum = nums[i] + nums[j]
            if sum == k: # 太好了，剛剛好!
                ans += 1
                i, j = i+1, j-1 # 左邊用了，往右；右邊用了，往左。
            if sum < k: # 加起來太小了，那左邊小的i要往右移
                i += 1
            if sum > k: # 加起來太大了，那右邊大的j要往左移
                j -= 1
        return ans

