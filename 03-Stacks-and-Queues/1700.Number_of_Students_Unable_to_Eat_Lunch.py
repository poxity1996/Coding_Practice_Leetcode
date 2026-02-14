#1700. Number of Students Unable to Eat Lunch (無法吃午餐的學生數量)
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        # 嘗試次數
        tired_count = 0
        sandwiches_index = 0
        
        while students_queue and tired_count < len(students_queue):
            if students_queue[0] == sandwiches[sandwiches_index]:
                students_queue.popleft()
                tired_count = 0
                sandwiches_index += 1
            else:
                students_queue.append(students_queue.popleft())
                tired_count +=1
                

        return len(students_queue)
