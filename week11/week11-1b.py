# week11-1b.py 學習計畫 Binary Tree - DFS 第2題 Easy題
# LeetCode 872. Leaf-Similar Trees
# 想知道 Binary Tree 裡的 leaf 組出來，是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def helper(root, leaves:list):
            if root == None: return # 如果沒有東西 什麼都不做
            if root.left == None and root.right == None: # 判斷葉子
                leaves.append(root.val) # 把值加入葉子
            helper(root.left, leaves) # 看左邊 
            helper(root.right, leaves) # 看右邊
        helper(root1, l1)
        helper(root2, l2)
        #print("root1", l1) debug
        #print("root2", l2) debug
        return l1 == l2
            
