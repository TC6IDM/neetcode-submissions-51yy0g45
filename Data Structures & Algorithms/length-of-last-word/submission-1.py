class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        for i in range(len(s.split(" "))):
            if len(s.split(" ")[-(i+1)]) != 0: return len(s.split(" ")[-(i+1)]) 

        return len(s.split(" ")[-1])