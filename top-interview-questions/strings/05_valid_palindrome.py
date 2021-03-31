class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
        s = s.lower()
        s_clean = []
        for c in s:
            if c in alphabet:
                s_clean += c
        s = "".join(s_clean)
        l = len(s)
        if l < 2:
            return True
        half_size = l/2
        for i in xrange(half_size):
            if s[i] != s[l - 1 - i]:
                return False
        return True
        