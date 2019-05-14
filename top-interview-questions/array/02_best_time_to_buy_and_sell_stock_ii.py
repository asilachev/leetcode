# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        
        for i in xrange(1, len(prices)):
            c = prices[i]
            p = prices[i-1]
            if p < c:
                result += c - p
                
        return result
