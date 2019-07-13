class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        ta = list(t)
        for i in xrange(len(s)):
            v = s[i]
            try:
                ta.pop(ta.index(v))
            except:
                return False
        return len(ta) == 0
