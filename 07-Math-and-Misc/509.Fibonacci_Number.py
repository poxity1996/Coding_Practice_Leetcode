class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        # a, b 初始化為 F(0), F(1)
        a,b = 0,1
        for _ in range(2,n+1):
            # 每次把前兩個加起來，然後往後移一格
            a,b = b,a+b
        return b