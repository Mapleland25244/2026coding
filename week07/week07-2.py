# week07-2.py 學習計畫 Stack 第2題
# LeetCode 735. Asteroid Collision
# 正的向右、負的向左，大的會把小的消滅。一樣大、一起死
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0 : # 正的往右，不會跟左邊相撞
                stack.append(a) # 直接塞
            else: # 負的往左，可能會跟 stack 裡的東西相撞「很多次」
                while stack and stack[-1] > 0: # 堆疊目前有存，且右邊正的、向右會相撞
                    if stack[-1] == -a: # 絕對值大小都相同，都消滅!
                        stack.pop() # 消滅、吐出來
                        a = 0 # 消滅
                        break # 離開迴圈
                    elif stack[-1] > -a:
                        a = 0 # 消滅右邊
                        break
                    else: # 左邊比較小，消滅左邊
                        stack.pop() # 消滅、吐掉(這裡不用break)
                if a != 0: stack.append(a)
        return stack
