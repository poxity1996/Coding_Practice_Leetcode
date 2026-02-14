# 232.Implement Queue using Stacks (用堆疊實作佇列)
class MyQueue:

    # 初始化queue
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    # 將stack_in的元素反過來移動到stack_out
    def move(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True 
        else:
            return False
    