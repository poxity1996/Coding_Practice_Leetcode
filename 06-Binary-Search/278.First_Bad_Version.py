# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1,n

        while left <= right:
            mid = (left+right)//2
            
            #True不一定是第一個壞掉版本
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1
                
        return left
        # 當迴圈結束時，left 會停在第一個讓 isBadVersion 為 True 的位置。
        # 此時 right 會停在最後一個為 False 的位置。
            