# week11-1a.py 學習計畫 Binary Tree - DFS 第2題 Easy題
# LeetCode 872. Leaf-Similar Trees
# 想知道 Binary Tree 裡的 leaf 組出來，是否都相同
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        a = []
        def helper(root):
            if root.left == None and root.right == None: # 判斷葉子
                a.append(root.val) # 把值加入a
            if root.left: helper(root.left) # 如果左邊有 
            if root.right: helper(root.right) # 如果右邊有
        helper(root1)
        a, b = [], a # 因為 a 塞好資料，要再開一個新的[]，並把舊的複製到新的
        helper(root2)
        #print("root1", a) debug
        #print("root2", b) debug
        return a == b
            
