# 時間複雜度:O(log n) 空間複雜度:O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <=0:
            return False
            
        while n%2 == 0:
            n //= 2

        return n==1


# 時間複雜度:O(log n) 空間複雜度:O(log n)，遞迴用法
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n<=0 or n%2 != 0:
            return False

        return self.isPowerOfTwo(n//2)

        