# 155. Min Stack (最小堆疊)
class MinStack:
    # 初始化 stack
    def __init__(self):
        self.stack = []
        self.stack_min =[]

    # 將val推入，判斷 stack_min 是否為空
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_min:
            self.stack_min.append(val)
        # 比較 stack_min[-1], val 的大小
        else:
            new_min = min(self.stack_min[-1],val)
            self.stack_min.append(new_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack_min:
            return self.stack_min[-1]