class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""

        for i in strs[0]:
            pref+=i
            for k in strs:
                if not k.startswith(pref):
                    return pref[:-1]
        return pref
        