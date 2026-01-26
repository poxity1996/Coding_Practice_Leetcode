# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        #判斷左右兩邊是否都有節點和是否有相同的值
        if not p or not q or p.val != q.val:
            return False

        #回傳兩邊的左節點和右節點
        return (self.isSameTree(p.left,q.left) and 
                self.isSameTree(p.right,q.right))