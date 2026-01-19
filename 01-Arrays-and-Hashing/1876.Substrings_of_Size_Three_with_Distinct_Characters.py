class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0 

        for i in range(len(s)-2): #要湊長度為3字串，最後2格不會跑到
            window = s[i:i+3]

            if len(set(window)) ==3: #用長度和set判斷字串是否重複
                count+=1
        
        return count