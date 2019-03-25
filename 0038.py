class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        numbers = ['','1']
        
        for i in range(2,n+1):
            number = numbers[i-1]
            next_number = ''
            count = 1
            
            char = number[0]
            for j in range(1,len(number)):
                if char == number[j]:
                    count = count + 1
                else:
                    next_number = next_number+ str(count) + char
                    char = number[j]
                    count = 1
            next_number = next_number+ str(count) + char
            
            numbers.append(next_number)
        return numbers[n]
                    
                
            
        
