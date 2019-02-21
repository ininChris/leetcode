import math
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 ==0:
            mid = length / 2
            return (nums[mid-1]+nums[mid])/2
        else:
            return nums[math.floor(length / 2)]

if __name__ == '__main__':
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    nums1 = [1, 3]
    nums2 = [2]
    s = Solution()
    result = s.findMedianSortedArrays(nums1, nums2)
    print(result)
