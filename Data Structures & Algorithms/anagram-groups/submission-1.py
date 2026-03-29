class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [[""]]
        start = False
        for i in strs:
            if not start:
                res[0] = [i]
                start = True
                continue
            
            counted = False
            for k in res:
                if sorted(i) == sorted(k[0]):
                    k.append(i)
                    counted = True
                    continue
            
            if not counted: res.append([i])
        
        return res
            
                



        