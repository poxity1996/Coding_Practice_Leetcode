# 933. Number of Recent Calls (最近請求次數)
from collections import deque
class RecentCounter:
    # 初始化序列
    def __init__(self):
        self.queue = deque()
    # 
    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[0] < t-3000:
            self.queue.popleft()

        return len(self.queue)
    