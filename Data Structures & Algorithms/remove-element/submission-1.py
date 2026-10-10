class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            elif nums[i] != val:
                i += 1
        return length
        return nums