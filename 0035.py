class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            num = nums[i]
            if num >= target:
                return i
        return len(nums)
        
