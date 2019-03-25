class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        sample = strs[0]
        for i in range(len(sample)):
            num = 0
            for str in strs:
                if i >=len(str) :
                    break
                if sample[i] != str[i]:
                    break
                else:
                    num = num +1
            if num != len(strs):
                return sample[:i]
        return sample
        
        
