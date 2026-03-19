# week04-4b.py (糶week04-3.py)
# LeetCode 3866. First Unique Even Element
# т皚 nums 柑 瞷1Ω案计琌街
        H = [0] * 200
        for nn in nums: # р皚硋ㄓ
            H[nn] += 1 # 参璸计秖
        for nn in nums: # ㄓΩ硋ㄓ
            if nn % 2 == 0 and H[nn] == 1: return nn # 案计 and 辅虫
