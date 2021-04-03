class Solution:
    def checkNeedle(self, h: str, n: str) -> bool:
        if len(h) < len(n):
            return False
        for idx, hc in enumerate(h):
            if hc != n[idx]:
                return False
            else:
                if len(n) == idx + 1:
                    return True            
        return True
            

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        if len(haystack) < len(needle):
            return -1

        needle_idx = 0
        for idx, c in enumerate(haystack):
            if c == needle[needle_idx]:
                if len(needle) == 1 or self.checkNeedle(haystack[idx + 1:], needle[1:]):
                    return idx
        return -1
