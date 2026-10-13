class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i < (len(arr) - 1):
                arr[i] = max(arr[i + 1:])
                i += 1
            elif i == (len(arr) - 1):
                arr[i] = -1
        """
        max_right = -1
        for i in range (len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)
        """
        return arr
            