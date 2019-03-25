class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [0]*len(triangle)
        for i in range(len(triangle)-2,-1,-1):
            line = triangle[i]
            next_line = triangle[i+1]
            for j in (range(len(line))):
                line[j] = min(next_line[j],next_line[j+1]) + line[j]
        return triangle[0][0]
                
