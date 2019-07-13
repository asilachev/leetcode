class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = 0
        l = len(digits)
        m = 10 ** (l-1)
        
        for i in xrange(l):
            result += digits[i]*m
            m /= 10
        
        result = result + 1
        out = []
        
        for s in str(result):
            out.append(int(s))
            
        return out
