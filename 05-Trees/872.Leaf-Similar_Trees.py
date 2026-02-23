# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #儲存node1,node2的葉子的序列
        path1, path2 = [], []

        def find(root, path):
            if not root:
                return None
            

            find(root.left,path)
            find(root.right,path)
            #如果是最底時，加入葉節點到path
            if not root.right and not root.left:
                path.append(root.val)
        
        find(root1,path1)
        find(root2,path2)

        return path1 == path2
