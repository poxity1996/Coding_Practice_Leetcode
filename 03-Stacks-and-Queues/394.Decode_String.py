# 394. Decode String (字串解碼)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        multi = 0

        for c in s:
            if c.isdigit():
                multi = multi*10+int(c)
            
            elif c == "[":
                stack.append([multi,res])
                multi,res = 0,""
            
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res

            else:
                res+=c

        return res
