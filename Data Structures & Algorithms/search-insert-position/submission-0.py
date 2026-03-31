class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for k,v in enumerate(nums):
            if v < target:
                if k == len(nums)-1:
                    return k+1
                if nums[k+1]> target:
                    return k+1
            if v > target and k == 0:
                return 0
            if v == target:
                return k
        