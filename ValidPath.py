class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if(source == destination): return True
        
        # build the Neighbor_list
        NB = dict()
        for (v, w) in edges:
            if(v not in NB): 
                NB[v] = [w]
            else:
                NB[v].append(w)
            if(w not in NB):
                NB[w] = [v]
            else:
                NB[w].append(v)
        # end for
        
        Vs = set([source])
        Vs_cur = set([source])
        Vt = set([destination])
        Vt_cur = set([destination])
        
        while(True): # pick the smaller of Vs_cur, Vt_cur
            
            if(len(Vs_cur) <= len(Vt_cur)):
                Vs_cur = self.get_nxt(NB, Vs, Vs_cur)
                if(len(Vs_cur) == 0): return False
                for w in Vs_cur:
                    if(w in Vt): return True
                    Vs.add(w)
            else:
                Vt_cur = self.get_nxt(NB, Vt, Vt_cur)
                if(len(Vt_cur) == 0): return False
                for w in Vt_cur:
                    if(w in Vs): return True
                    Vt.add(w)
            
        # end for
        
        return False
    
    
    def get_nxt(self, NB, Vs, Vs_cur):
        # get the next set V_nxt
        Vs_nxt = set()
        for v in Vs_cur:
            for w in NB[v]:
                if(w not in Vs):
                    Vs_nxt.add(w)
            # end for w
        # end for v
        
        return Vs_nxt
        
