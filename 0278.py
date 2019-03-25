# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 0
        mid = n
        while n>1:
            mid = math.ceil(n/2)
            print(base+mid)
            flag =  isBadVersion(base + mid)
            if not flag:
                base = base + mid
            n = mid
        return base+mid
