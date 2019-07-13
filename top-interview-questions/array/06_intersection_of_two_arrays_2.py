class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        out = []

        for i in xrange(l1):
            x = nums1[i]
            try:
                idx = nums2.index(x)
                nums2[idx] = None
                out.append(x)
            except:
                pass
                
        return out
