class Solution(object):
    
    grid = []
    cnt = 0
    n, m = 0, 0
    start, end = None, None
    numEmpty = 0
    
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.n = len(grid)
        self.m = len(grid[0])
        self.cnt = 0
        
        numEmpty = 0
        for i in range(self.n):
            for j in range(self.m):
                if(grid[i][j] == 1): 
                    self.start = [i, j]
                    numEmpty += 1
                elif(grid[i][j] == 2):
                    self.end = [i, j]
                    numEmpty += 1
                elif(grid[i][j] == 0):
                    numEmpty += 1
        # end for i, j
        self.numEmpty = numEmpty
        
        if(self.start == None) or (self.end == None): return 0
        
        self.DFS(self.start[0], self.start[1]) 
        return self.cnt # number of solutions    
        
        
    def DFS(self, i, j):  
        # start with START, walk all empty nodes, reach END
        # check its four neighbors, find candidate next mvoes
        if(i < 0) or (i >= self.n) or (j < 0) or (j >= self.m): 
            return
        
        if(self.grid[i][j] == 3) or (self.grid[i][j] == -1): return
        
        if(self.grid[i][j] == 2):
            if(self.numEmpty == 1): self.cnt += 1
            return 
    
        self.grid[i][j] = 3
        self.numEmpty -= 1
            
        self.DFS(i-1, j)
        self.DFS(i+1, j)
        self.DFS(i, j+1)
        self.DFS(i, j-1)
    
        # self.empty.add(str([i0, j0])) # after it, add it back    
        self.grid[i][j] = 0
        self.numEmpty += 1
        
        return  
       
