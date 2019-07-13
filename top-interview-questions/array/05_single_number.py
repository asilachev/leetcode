class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in xrange(len(nums)):
            k = nums[i]
            try:
                _ = d[k]
                del d[k]
            except:
                d[k] = k
        return list(d.keys())[0]
