# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 定義內部的輔助函式：同時處理「高度計算」與「平衡判斷」
        def check_height(node):
            if not node:
                return 0

            left = check_height(node.left)
            if left == -1: 
                return -1  #已經失衡就往傳

            right = check_height(node.right)
            if right == -1:
                return -1  #已經失衡就往傳
            
            #判斷高度是否失衡
            if abs(left-right) > 1:
                return -1 

            return max(left,right)+1
        
        #判斷最後的高度不是 -1，就代表整棵樹是平衡的
        return check_height(root) != -1
