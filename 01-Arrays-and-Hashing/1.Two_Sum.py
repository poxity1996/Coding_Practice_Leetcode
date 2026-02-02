class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #紀錄未出現的值
        history = {}

        for i,x in enumerate(nums):
            y = target - x

            if y in history:
                return [history[y],i]
            
            history[x] = i
