class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum  = 0
        answer = nums[0]
        for num in nums:
            if sum >= 0:
                sum = sum + num
            else:
                sum = num
            answer = max(answer,sum)
        return answer
        
