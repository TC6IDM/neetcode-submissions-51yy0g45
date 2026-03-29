import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        middle = math.ceil((start+end)/2)
        
        while True:
            if start == end and nums[middle] != target: return -1
            if nums[middle] == target: 
                return middle

            if nums[middle] < target:
                start = middle+1
                end = end
            
            if nums[middle] > target:
                end = middle-1
                start = start
            
            middle = math.floor((start+end)/2)
        