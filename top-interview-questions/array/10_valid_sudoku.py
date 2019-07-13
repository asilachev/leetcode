class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        q = [[{} for k in range(3)] for i in range(3)]
        t = [{} for i in range(9)]
        
        for i in xrange(len(board)):
            d = {}
            qi = int(i/3)
            for k in xrange(len(board[i])):
                v = board[i][k]                
                qk = int(k/3)
                
                if v == '.':
                    continue              
                
                try:
                    _ = t[k][v]
                    return False
                except:
                    t[k][v] = v                
                try:
                    _ = d[v]
                    return False
                except:
                    d[v] = v
                    
                try:
                    _ = q[qi][qk][v]
                    return False
                except:
                    q[qi][qk][v] = v                    
                    
        return True
