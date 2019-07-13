class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = []
        l = len(nums)
        for i in xrange(l):
            n = nums[i]
            c.append(n)
            if i != 0:
                for k in xrange(i):
                    if (c[k] + n) == target:
                        return [nums.index(c[k]), i]
