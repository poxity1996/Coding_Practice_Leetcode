# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#遞迴解法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #往後找，直到找到最後一個節點
        rev_head = self.reverseList(head.next)
        tail = head.next 
        tail.next = head
        head.next = None

        #新的頭 rev_head 會一路被傳回最上層，不做任何改動
        return rev_head
    

