class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = -1 if (x < 0) else 1
        x = n*x
        s = list(str(x))
        l = len(s)
        for i in xrange(int(l/2)):
            o = s[i]
            d = l - (1 + i)
            s[i] = s[d]
            s[d] = o

        r = int(''.join(s))*n
        if r < -2**31 or r > 2**31-1:
            r = 0
        return r
