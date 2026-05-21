# week13-3.py 學習計畫 Heap / Priority Queue 第1題
# LeetCode 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 先用作弊的寫法示範一次
        # nums.sort(reverse = True)
        # return nums[k-1] 
        
        # 要用 Heap 資料結構，可以找出最小的數
        # heapify(nums)
        # while nums:
        #    print(heappop(nums))

        # 最後用這個版本
        heapify(nums) # 變成 heap 資料結構 時間複雜度:O(logN)
        for i in range(len(nums)-k):
            heappop(nums) # 吐掉不用的 N-k個數
        return heappop(nums) # 剩下的那個，就是第k大的。