class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        cur1s = 0
        for i in nums:
            if i == 1:
                cur1s +=1
                if max1s<cur1s: max1s = cur1s
            else:
                if max1s<cur1s: max1s = cur1s
                cur1s = 0
        
        return max1s
        