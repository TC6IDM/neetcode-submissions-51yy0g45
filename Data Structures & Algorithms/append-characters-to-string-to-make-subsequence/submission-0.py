class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_counter = 0
        for i in s:
            if t == "": return len(t) - t_counter
            if t_counter >= len(t) or i != t[t_counter]:
                pass
            else:
                t_counter+=1
        
        return len(t) - t_counter