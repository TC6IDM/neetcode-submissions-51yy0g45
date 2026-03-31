class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newnums=[]
        for i in nums:
            if i!=val: newnums.append(i)

        for i in range(len(newnums)):
            nums[i] = newnums[i]
        return len(newnums)
        