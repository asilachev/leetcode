class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        x = []
        for i in xrange(l):
            for k in xrange(l):
                x.append(matrix[i][k])
        rx = list(reversed(x))
        
        for i in xrange(l):
            for k in xrange(l):
                matrix[k][i] = rx[l-k-1 + i*l]
            
