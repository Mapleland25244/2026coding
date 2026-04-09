# week07-4.py 學習計畫 Stack 第3題，有點難
# LeetCode 394. Decode String
# 將字串解碼 數字代表「重複的次數」會把右邊「方括號」裡的字串重複
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # 利用 stack 處理 「方括號」及對應的「數字」
        curr_num = 0 # 現在的數字
        curr_str = [] # 現在的字串
        for c in s:
            if c.isdigit(): # 如果數字，就組合起來
                curr_num = curr_num * 10 + int(c)
            elif c.isalpha(): # 如果是字母 就讓「字串」變長
                curr_str.append(c)
            elif c == '[': # 新的開始
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = []
                curr_num = 0
            elif c == ']': # 結束要解碼了
                num = stack.pop() # 之前在 [ 方括號塞的 num
                prev_str = stack.pop() # 之前在 [ 方括號塞的 str
                curr_str = prev_str + curr_str * num # 解碼
        return "".join(curr_str)


