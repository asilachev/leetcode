class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in xrange(len(nums)):
            k = nums[i]
            try:
                _ = d[k]
                return True
            except:
                d[k] = k
        return False
