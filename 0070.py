class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pp = 1
        p = 2
        if n == 1:
            return pp
        if n == 2:
            return p
        for i in range(3,n+1):
            temp = p
            p = p + pp
            pp = temp
            
        return p
        
