# 344. Reverse String (反轉字串)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #只能園地修改用雙指針
        left = 0
        right = len(s)-1
        
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1

        return s