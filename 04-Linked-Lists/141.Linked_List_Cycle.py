# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        # 設一個快慢針
        slow = head
        fast = head

        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            
            #如果是環形列表快針一定會追上慢針
            if slow == fast:
                return True

        return False
