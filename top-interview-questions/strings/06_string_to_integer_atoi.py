class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        MAX_INT = 2147483648
        DIGITS = "0123456789"
        SIGNS = "-+"

        while True:
            if len(s) > 0 and s[0] == " ":
                s = s[1:]
            else:
                break
        if len(s) == 0 or s[0] not in DIGITS + SIGNS:
            return 0
        
        result = s[0]
        i = 1
        while i < len(s):
            if s[i] in DIGITS:  
                result += s[i]
                i += 1
            else:
                break

        negative = 1
        if result[0] == "-":
            negative = -1
        if result[0] in SIGNS:
            result = result[1:]
        if len(result) == 0:
            return 0
        result_int = int(result) * negative
        if result_int < MAX_INT * -1:
            return MAX_INT * -1
        if result_int > MAX_INT - 1:
            return MAX_INT - 1
        return result_int