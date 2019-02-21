class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    def threeSum(self, nums, target):
        nums.sort()
        map = {}
        for i in range(len(nums)):
            one = nums[i]
            result = self.twoSum(nums[i+1:], 0-one)
            for item in result:
               if not one in map:
                   map[one] = {}
               map[one][item[0]]=item[1]
        print(map)
        result = []
        for k,v in map.items():
            for sk,sv in v.items():
                result.append([k,sk,sv])
        return result
        
    def twoSum(self, nums, target):
        map = {}
        data = []
        if nums == None:
            return data
        for index in range(len(nums)):
            number = nums[index]
            if number in map: 
                data.append([map[number], number])
            result = target - number 
            map[result] = number

        return data
