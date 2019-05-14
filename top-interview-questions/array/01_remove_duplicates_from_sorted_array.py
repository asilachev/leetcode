# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        for i in range(1, len(nums)):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1
