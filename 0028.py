class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
 
        length = len(needle)
        for i in range(len(haystack)):
            
            offset = length -1
            if (i+offset) >= len(haystack):
                return -1
            if haystack[i] != needle[0]:
                continue
            while i <= (i+offset):
                if haystack[i+offset] == needle[offset]:
                    if offset == 0:
                        return i
                    else:
                        offset = offset -1
                else:
                    break
        return -1
                
                
            
        
