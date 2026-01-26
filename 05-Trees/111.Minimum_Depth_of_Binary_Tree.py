# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:
            return max(left,right)+1

        return min(right,left)+1
    
#BFS
import collections
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        result = 0

        queue = collections.deque([root])

        while queue:
            result+=1
            level_len = len(queue)

            for _ in range(level_len):
                node = queue.popleft()

                if not node.left and not node.right:
                    return result

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

