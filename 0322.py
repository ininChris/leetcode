class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        mins = [-1]*(amount+1)
        mins[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if coin > i:
                    continue
                prev = i-coin
                if mins[prev] == -1:
                    continue
                if mins[i] == -1:
                    mins[i]=mins[prev]+1
                else:
                    mins[i]=min(mins[i],mins[prev]+1)
        return mins[amount]
                
                
                    
                
                
            
