class Solution:
    def isValid(self, s: str) -> bool:
        op = ["[","{","("]
        cl = ["]","}",")"]

        st = []
        for i in range(len(s)):
            if s[i] in op: st.append(s[i])
            if s[i] in cl: 
                if not st: return False
                if s[i] == ")" and st[len(st)-1]  != "(": return False
                if s[i] == "}" and st[len(st)-1]  != "{": return False
                if s[i] == "]" and st[len(st)-1]  != "[": return False
                st.pop()
        if len(st) > 0: return False
        return True
