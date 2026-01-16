# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        #設偶頭，基偶指標
        odd = head   
        even = head.next 
        even_head = even

        while even and even.next:
            #奇數節點指向下一個奇數
            odd.next = even.next
            odd = odd.next

            #偶數節點指向下一個偶數
            even.next = odd.next
            even = even.next 

        #基指指向偶頭
        odd.next = even_head

        return head