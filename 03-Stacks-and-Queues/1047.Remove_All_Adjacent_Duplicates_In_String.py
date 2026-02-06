class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for i in s:
            #如果當前字元與 stack 頂端元素相同，就移除頂端的元素
            if stack and stack[-1] == i:
                stack.pop()

            else:
                stack.append(i)

        return "".join(stack)
