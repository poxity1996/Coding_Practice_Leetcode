# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
# 廣度優先搜尋（BFS） 演算法
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        # 初始化隊列（Queue），並將根節點放入
        queue = collections.deque([root])

        while queue:
            level_size = len(queue)
            current_level = []
            #處理目前這一層的所有節點
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                #將下一層的子節點放入隊列中
                #先放左子節點，再放右子節點，確保從左到右的順序
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result