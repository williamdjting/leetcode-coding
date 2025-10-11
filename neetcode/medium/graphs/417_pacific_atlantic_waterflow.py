from typing import List, DefaultDict, Optional

from collections import defaultdict

class Solution:
    def __init__ (self):
        return
    # my solution
    from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def dfs(r: int, c: int, seen: List[List[bool]]) -> None:
            if seen[r][c]:
                return
            seen[r][c] = True

            # up
            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfs(r - 1, c, seen)
            # down
            if r + 1 < m and heights[r + 1][c] >= heights[r][c]:
                dfs(r + 1, c, seen)
            # left
            if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfs(r, c - 1, seen)
            # right
            if c + 1 < n and heights[r][c + 1] >= heights[r][c]:
                dfs(r, c + 1, seen)

        # seed from pacific (top row, left col)
        for r in range(m):
            dfs(r, 0, pac)
        for c in range(n):
            dfs(0, c, pac)

        # seed from atlantic (bottom row, right col)
        for r in range(m):
            dfs(r, n - 1, atl)
        for c in range(n):
            dfs(m - 1, c, atl)

        # intersection
        res: List[List[int]] = []
        for r in range(m):
            for c in range(n):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res

    
    
    # the actual solution
    # https://chatgpt.com/share/68e5fc6e-5610-8008-ad4e-8a1229a95af7
    
    # my solution , incorrect - needs flood fill
    # def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    #     '''
    #     the island  which is the graph matrix touches the top, left = Pacific and the right, bottom = Atlantic
        
    #     m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
        
    #     rain can travel N, S, E , W neighboring cell's height is less than or equal to the current cell's height.
        
    #     Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    #     '''
        
    #     rowSize = len(heights)
    #     colSize = len(heights[0])
        
    #     if rowSize < 0 or rowSize > len(heights) or colSize < 0 or colSize > len(heights[0]):
    #         return -1
        
    #     graph = {}

    #     for i in range(rowSize):
    #         graph[i] = []

    #     for u, v in heights:
    #         # go both ways
    #         graph[v].append(u) #v-> u 
    #         graph[u].append(v) #u-> v 
        
    #     def dfs(self, graph: List[List[int]] ) -> int:
    #         height = 0
            
    #         val = graph[r][c] 
    #              # height above sea level of the cell at coordinate (r, c)
    #         if height <  val:
    #             height = val
    #         else:
    #             height  = max(val , height)
            
    #         for neighbour in graph[r][c]:
    #             if not dfs(neighbour):
    #                 return False

    #         return r, c
            
    #     res : List[tuple[int]] = []
        

    #     for r in range(rowSize):
    #         for c in range(colSize):
    #              if not dfs(graph):
    #                 res.append[(r, c)]
                        
    #     return res




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