class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        c = nums[:]
        for i in xrange(l):
            n = i + k
            while n >= l:
                n -= l
            nums[n] = c[i]
