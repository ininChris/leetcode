class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        if len(nums) ==1:
            return nums[0]
        max_amounts = [-1]*len(nums)
        max_amounts[0] = nums[0]
        max_amounts[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            tr = max_amounts[i-2] + nums[i]
            fr = max_amounts[i-1]
            max_amounts[i] =  max(tr,fr)
        
        return max_amounts[len(max_amounts)-1]
            
        
