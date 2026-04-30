# week10-3.py 學習計畫 Binary Tree 第3題
# LeetCode 1448. Count Good Nodes in Binary Tree
# 遇Tree 使用 「函式呼叫函式」
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        rootmax = root.val
        def helper(root, rootmax): # 記得祖先最大的max
            if root == None: return 0
            count = 0
            if root.val >= rootmax:
                count += 1
                rootmax = root.val
            count += helper(root.left, rootmax)
            count += helper(root.right, rootmax)
            return count
        return helper(root, rootmax)
