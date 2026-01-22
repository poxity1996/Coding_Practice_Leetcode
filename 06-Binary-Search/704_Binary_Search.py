# 704. Binary Search
# 分類: 06-Binary-Search
# 時間複雜度: O(log n) - 每次排除一半搜尋範圍
# 空間複雜度: O(1) - 僅使用常數個變數
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            #設定範圍的中間點
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            #比較mid跟target的大小
            elif nums[mid] > target:
                right =mid-1
            else:
                left = mid+1
        return -1

            