class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def backspace(string):
            stack = []
            for i in string:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return "".join(stack)

        return backspace(s) == backspace(t)
