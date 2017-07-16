class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        print "s", s
        print "r", r
        print "overflow", (r < 2**31)
        return s*r * (r < 2**31)

solution = Solution()
print solution.reverse(321)
