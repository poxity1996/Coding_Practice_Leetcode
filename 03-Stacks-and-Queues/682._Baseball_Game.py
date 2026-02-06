class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if stack and i == "C":
                stack.pop()

            elif stack and i == "D":
                stack.append(stack[-1]*2)

            elif len(stack) >= 2 and i =="+":
                stack.append(stack[-1]+stack[-2])

            else:
                stack.append(int(i))

        return sum(stack)

