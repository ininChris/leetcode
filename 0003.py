class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        max_count = 0
        current_count =0
        start_index = 0
        for i in range(len(s)):
            c = s[i]
            if c in map:
                start_index = map[c] + 1 if map[c]+1>start_index else start_index
            map[c] = i
            current_count = i + 1 - start_index
            #print(c,":s:",start_index,":i:",i)
            max_count = current_count if current_count > max_count else max_count
        print(current_count)
        print(max_count)
        return max_count
        
