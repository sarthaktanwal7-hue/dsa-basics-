class Solution(object):
    def reverse(self, x):
        nn = 0

        if x < 0:
            x = x * -1
            while x > 0:
                d = x % 10
                nn = nn * 10 + d
                x //= 10
            nn = nn * -1

        else:
            while x > 0:
                d = x % 10
                nn = nn * 10 + d
                x //= 10

        if nn > 2147483647 or nn < -2147483648:
            return 0
        else:
            return nn


        """
        :type x: int
        :rtype: int
        """
        
