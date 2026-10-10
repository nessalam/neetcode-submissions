class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        i = 0
        top = 0
        while i < (len(nums) - 1):
            if nums[i] == 1:
                count += 1
            else:
                top = count
                count = 0
            i += 1
        if i == (len(nums) - 1) and nums[i-1] and nums[(len(nums) - 1)] == 1:
            top += 1
        return top