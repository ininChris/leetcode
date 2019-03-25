class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point = -1
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and num == nums[i-1] and point == -1:
                point = i-1
            else:
                if num > nums[point]:
                    nums[point+1]=num
                    point = point +1
        if point == -1:
            return len(nums)
        return point+1
            
