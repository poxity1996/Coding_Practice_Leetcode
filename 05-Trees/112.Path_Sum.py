# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        #讓目標數字持續往下減法
        remain = targetSum - root.val
        #最底時比較最後一個數字是否等於remain
        if not root.left and not root.right:
            return targetSum == root.val
        
        # 只要「左子樹」或「右子樹」其中一條路徑成立即可
        return(self.hasPathSum(root.left,remain) or 
               self.hasPathSum(root.right,remain))