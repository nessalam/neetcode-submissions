class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = nums1[0 : m]   
        R = nums2[0 : n]

        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if L[i] <= R[j]:
                nums1[k] = R[j]
                j -= 1
            else:
                nums1[k] = L[i]
                i -= 1
            k -= 1
        
        while i >= 0:
            nums1[k] = L[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = R[j]
            j -= 1
            k -= 1

        print(nums1)