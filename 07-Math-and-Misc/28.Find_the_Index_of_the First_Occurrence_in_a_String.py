
#使用sliding window的解法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        for i in range(len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1
    
# 內建函式解法find()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)