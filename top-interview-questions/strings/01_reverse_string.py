class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in xrange(int(l/2)):
            o = s[i]
            idx = l - (i+1)
            s[i] = s[idx]
            s[idx] = o
