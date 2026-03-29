class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        
        sol = []
        for i in range(k):
            sol.append(max(freq, key = freq.get))
            freq[max(freq, key = freq.get)] = 0

        return sol

        