# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])
        # 開始層級遍歷 (BFS)
        while queue:
            level_size = len(queue)
            # 初始化該層的累加總和變數
            current_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #計算平均值後存入表
            result.append(current_level_sum/level_size)
        return result