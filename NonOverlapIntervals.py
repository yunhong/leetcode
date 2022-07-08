class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        
        end = float('-inf')
        erased = 0
        intervals.sort(key = lambda item: item[1])
        
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                erased += 1
        # end for 
        
        return erased
