class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newlist = [-1]*len(arr)

        largest = arr[-1]
        for i in range(len(arr)):
            if i == 0:
                newlist[-(i+1)] = -1
            else:
                newlist[-(i+1)] = largest
            if arr[-(i+1)] > largest:
                largest = arr[-(i+1)]
        
        print(newlist)
        return newlist