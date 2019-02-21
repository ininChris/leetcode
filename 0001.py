class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index in range(len(nums)):
            if nums[index] in map: 
                return [map[nums[index]], index]
            result = target - nums[index]
            map[result] = index

if __name__ == "__main__" :
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)
