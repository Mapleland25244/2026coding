# week09-3.py 學習計畫 Linked List 第3題 Easy 題 (使用「遞迴」Recursion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head # 終止條件
        newhead = head.next
        ans = self.reverseList(head.next) # 函式呼叫函式
        newhead.next, head.next = head, None
        return ans
