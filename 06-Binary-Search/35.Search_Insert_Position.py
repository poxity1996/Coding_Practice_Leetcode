class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return left
        # 當迴圈結束仍未找到 target 時，left 指針會停在「第一個大於 target 的元素」位置
        # 這剛好就是 target 應該被插入的索引位置