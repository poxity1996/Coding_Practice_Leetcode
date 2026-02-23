# 437. Path Sum III(路徑總和)

# 暴力解:
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node,curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            res = 1 if curr_sum == targetSum else 0

            res += dfs(node.left,curr_sum)
            res += dfs(node.right,curr_sum)

            return res

        def count(node):
            if not node:
                return 0

            return dfs(node,0) + count(node.left) + count(node.right)

        
        return count(root)

