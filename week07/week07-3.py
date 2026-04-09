# week07-3.py 學習計畫 Stack 第1題
# LeetCode 2390. Removing Stars From a String

class Solution:
    def removeStars(self, s: str) -> str:
        stack = [] # 放答案堆疊陣列 LIFO
        for c in s: # 逐一取出字母 c 再判斷
            if c == '*': stack.pop() # 遇到星號，吐掉1個字母
            else: stack.append(c) # 把不是星號的字母，塞進去
        return "".join(stack) # 用 join() 把陣列 join 成字串
