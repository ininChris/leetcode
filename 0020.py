class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_map = {')':'(',']':'[','}':'{'}
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0 or p_map[c] != stack[len(stack)-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0
                
                
                
        
