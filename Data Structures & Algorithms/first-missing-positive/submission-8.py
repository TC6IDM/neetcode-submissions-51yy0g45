class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        count =nums[0]
        print(nums)
        start = False
        for i in nums:
            if i<=0: continue
            if start == False:
                if i>1: return 1
                start = True
                count = i
                
            print(i)
            print(count)
            print()
            if i != count:
                count +=1
                if count != i:
                    return count
                
        if count <=0: return 1
        return count+1
        