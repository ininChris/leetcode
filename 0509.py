class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        pp = 0
        p = 1
        if N == 0:
            return pp
        if N == 1:
            return p
        for i in range(2,N+1):
            temp = p
            p = p + pp
            pp = temp
            
        return p
