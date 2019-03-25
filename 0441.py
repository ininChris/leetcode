class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        index = 0
        
        while True:
            index+=1
            if n-index<0:
                break
            else:
                 n = n -index
            
        return index-1
        
