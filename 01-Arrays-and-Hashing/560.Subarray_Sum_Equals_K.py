
# 560. Subarray Sum Equals K(560. 和為 K 的子數組)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前綴和:出現次數，初始值代表還沒開始走
        prefix = {0:1} 
        # 從頭到當前位置的總和
        curr_sum = 0
        res = 0


        for i in range(len(nums)):
            curr_sum += nums[i]
            # 查有沒有符合的子陣列
            res += prefix.get(curr_sum - k, 0)
            # 記錄當前前綴和
            prefix[curr_sum]  = prefix.get(curr_sum,0)+1
        
        return res