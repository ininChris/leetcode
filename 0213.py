class Solution:
    def rob_region(self, nums, start, end):
        nums_slice = nums[start:end]
        if len(nums_slice) ==0:
            return 0
        if len(nums_slice) ==1:
            return nums_slice[0]
        max_amounts = [-1]*len(nums_slice)
        max_amounts[0] = nums_slice[0]
        max_amounts[1] = max(nums_slice[0],nums_slice[1])
        
        for i in range(2,len(nums_slice)):
            tr = max_amounts[i-2] + nums_slice[i]
            fr = max_amounts[i-1]
            max_amounts[i] =  max(tr,fr)
        result = max_amounts[len(max_amounts)-1]
        return result
        
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return  max(nums[0],nums[1])
        
        return max(self.rob_region(nums,1,len(nums)),self.rob_region(nums,0,len(nums)-1))
