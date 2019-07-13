class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s)
        d = {}
        for i in xrange(len(a)):
            v = a[i]
            try:
                _ = d[v]
                d[v] = None
            except:
                d[v] = i
        vals = d.values()
        r = None
        for i in (xrange(len(vals))):
            v = vals[i]
            if v == None:
                continue
            if r == None:
                r = v
            if v < r:
                r = v
        return -1 if r == None else r
