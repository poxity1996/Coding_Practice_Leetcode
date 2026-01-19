class Solution:
    def isValid(self, s: str) -> bool:
        # 建立括號對應表，Key 為右括號，Value 為對應的左括號
        pair_map ={")":"(",
                   "]":"[",
                   "}":"{"}

        stack = []

        for char in s:
            # 如果是右括號，進行匹配檢查
            if char in pair_map:
                if stack and pair_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                #左括號推入stack等待匹配
                stack.append(char)

        return not stack

