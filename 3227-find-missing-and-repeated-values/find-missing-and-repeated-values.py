class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr=[e for sublist in grid for e in sublist]
        arr.sort()
        n=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                n.append(arr[i])
                arr.remove(arr[i])
                break
        arr.append(1000000)
        for i in range(len(arr)):
            if i+1!=arr[i]:
                n.append(i+1)
                break
        return n
        