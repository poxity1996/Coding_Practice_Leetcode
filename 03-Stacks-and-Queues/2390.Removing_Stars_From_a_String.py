# 2390. Removing Stars From a String (從字符串中移除星號)
# 堆疊
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in s:
            if stack and i =="*":
                stack.pop()

            else:
                stack.append(i)

        return "".join(stack)
    
# 雙指針
class Solution:
    def removeStars(self, s: str) -> str:
        s_list = list(s)
        j = 0

        for i in range(len(s_list)):
            if s_list[i] =="*":
                j -= 1

            else:
                s_list[j] = s_list[i]
                j+=1

        return "".join(s_list[:j])