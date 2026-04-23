# week09-6.py 厩策璸礶 Linked List 材2肈
# LeetCode 328. Odd Even Linked List 案计帮计帮﹃癬ㄓ
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        odd = head # 材计
        even = head.next # 材案计
        evenhead = even # 案计繷рウ钡计
        while even != None and even.next != None:
            odd.next = even.next # 计琌案计
            odd = odd.next # 计簿笆计
            even.next = odd.next # 案计琌计
            even = even.next # 案计簿笆计
        odd.next = evenhead # р案计繷钡计Ю
        return head
