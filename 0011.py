import math
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        anser = 0
        i = 0
        j = len(height) - 1
        while i<j:
            h = min(height[i],height[j])
            w = j - i
            anser = max(anser, h*w)
            if height[i]>height[j]:
                j = j -1
            else:
                i = i + 1
        return anser
