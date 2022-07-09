class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    board = []
    
    pos24_list = [0] * 81
    
    for index in range(81): # index = i0 + 9 * j0
        i0 = index % 9
        j0 = index / 9
        res = []
        for i in range(9):
            if(i != i0):
                res.append([i, j0]) 
        for j in range(9):
            if(j != j0):
                res.append([i0, j])
        I0 = 3 * int(i0/3)
        J0 = 3 * int(j0/3)
        for i in range(I0, I0+3):
            for j in range(J0, J0+3):
                if([i, j] != [i0, j0]):
                    res.append([i, j])
        pos24_list[index] = res
    
    
    def solveSudoku(self, board): # input element char
        self.board = board
        for i in range(9):
            for j in range(9):
                if(board[i][j] == '.'): board[i][j] = 0
                else: board[i][j] = int(board[i][j])
        
        self.DFS() 
        
        for i in range(9):
            for j in range(9):
                if(board[i][j] == 0): board[i][j] = '.'
                else: board[i][j] = str(board[i][j])

        
    def DFS(self):
        empty_nodes = self.get_empty_nodes()
        if(len(empty_nodes) == 0): return True
        board = self.board

        node_nxt = None
        candidates_nxt = None
        size_nxt = 10
        
        for node in empty_nodes:
            candidates = self.get_candidates(node)
            
            if(len(candidates) == 0): return False
            if(len(candidates) < size_nxt):
                size_nxt = len(candidates)
                node_nxt = node
                candidates_nxt = candidates
        # end for loop, find node_nxt as min candidate choices
        [i, j] = node_nxt
        for v in candidates_nxt:
            board[i][j] = v
            res = self.DFS()
            if(res): return True
        # end for loop  
        board[i][j] = 0 # use it to represent '.'
        return False
            
    def get_candidates(self, node):
        [i0, j0] = node
        index = i0 + 9 * j0
        pos24 = self.pos24_list[index]
        
        board = self.board
        flag9 = 9 * [False]
        for [i, j] in pos24:
            if(board[i][j] != 0):
                c = board[i][j]
                flag9[c-1] = True
        # end for loop
        candidates = []
        for v in range(1, 10):
            if(not flag9[v-1]):
                candidates.append(v)
        return candidates
        
    def get_empty_nodes(self):
        board = self.board;
        empty_nodes = []
        for i in range(9):
            for j in range(9):
                if(board[i][j] == 0): 
                    empty_nodes.append([i, j])
        return empty_nodes
