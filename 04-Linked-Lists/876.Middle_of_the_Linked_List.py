# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        #設快慢針
        slow = head
        fast = head
        #快針跑完慢針正好在鍊表的一半
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
