import pdb
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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

if __name__ == "__main__":
    s = Solution()
    result = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
