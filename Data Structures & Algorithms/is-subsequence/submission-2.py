class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_counter = 0
        for i in t:
            if s == "": return True
            if s_counter >= len(s) or i != s[s_counter]:
                pass
            else:
                s_counter+=1
        return s_counter == len(s)

        