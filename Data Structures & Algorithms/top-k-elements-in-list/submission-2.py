class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        dic = sorted(dic, key=dic.get, reverse=True)

        return dic[0:k]