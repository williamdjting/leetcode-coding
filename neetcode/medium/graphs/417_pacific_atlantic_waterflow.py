from typing import List, DefaultDict, Optional

from collections import defaultdict

class Solution:
    def __init__ (self):
        return
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        the island  which is the graph matrix touches the top, left = Pacific and the right, bottom = Atlantic
        
        m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
        
        rain can travel N, S, E , W neighboring cell's height is less than or equal to the current cell's height.
        
        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
        '''
        
        rowSize = len(heights)
        colSize = len(heights[0])
        
        if rowSize < 0 or rowSize > len(heights) or colSize < 0 or colSize > len(heights[0]):
            return -1
        
        
        def dfs(self, graph: List[List[int]] ) -> int:
            
        
        graph : DefaultDict[List[List[int]]]= defaultdict(list)
        height = 0
        for r in range(rowSize):
            for c in range(colSize):
                 val = heights[r][c] 
                 # height above sea level of the cell at coordinate (r, c)
                 if height <  val:
                     height = val
                     
                 else:
                     height  = max(val , height)
                
                        




heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

'''
[[1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]]
'''

sol = Solution()

result = sol.pacificAtlantic(heights)

print(result) #returns a 2D list of grid coordinates