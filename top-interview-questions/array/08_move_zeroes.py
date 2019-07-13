class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        nz = 0
        for i in xrange(l):
            n = nums[i]
            if n == 0:
                nz += 1
            else:
                if nz:
                    nums[i-nz] = n
        for i in xrange(l - nz, l):
            nums[i] = 0
