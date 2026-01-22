class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right = 1,num

        while left <= right:
            mid = (left+right)//2
            x = mid*mid

            if x == num:
                return True
            elif x > num:
                right = mid-1
            else:
                left = mid+1

        return False

            
