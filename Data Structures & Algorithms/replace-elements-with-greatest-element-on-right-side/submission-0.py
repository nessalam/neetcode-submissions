class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0 
        for i in range(len(arr)):
            if i < (len(arr) - 1):
                arr[i] = max(arr[i + 1:])
                i += 1
            elif i == (len(arr) - 1):
                arr[i] = -1
        return arr
            