# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 紀錄全局最大直徑
        self.max_d = 0

        def get_diameter(node):
            if not node:
                return 0

            left = get_diameter(node.left)
            right = get_diameter(node.right)

            #長路徑 = 左深 + 右深
            self.max_d = max(self.max_d,left+right)

            return max(left,right)+1

        get_diameter(root)
        return self.max_d