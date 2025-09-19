# most common pattern
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            # stop at bounds, water, or visited
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != "1":
                return
            # mark visited by sinking the land
            grid[r][c] = "0"
            # explore 4-neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)       # sink this island
                    count += 1      # and count it
        return count

# Test
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("answer", Solution().numIslands([row[:] for row in grid]))  # 1




# # solution using my attempt (correct solution)
# from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
        
#         ROWS, COLS = len(grid), len(grid[0])
#         numberOfIslands = 0

#         def dfs(r: int, c: int) -> None:
#             # bounds or water/visited
#             if (r < 0 or r >= ROWS or
#                 c < 0 or c >= COLS or
#                 grid[r][c] != "1"):
#                 return

#             # mark visited (sink)
#             grid[r][c] = "#"

#             # explore neighbors (up, down, left, right)
#             dfs(r+1, c)
#             dfs(r-1, c)
#             dfs(r, c+1)
#             dfs(r, c-1)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1":
#                     dfs(r, c)          # sink this island
#                     numberOfIslands += 1

#         return numberOfIslands

# my attempt
# from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         # Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and 
#         # '0's (water), return the number of islands.

#         # An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#         # You may assume all four edges of the grid are all surrounded by water.


#         if not grid or not grid[0]:
#             return 0
        
#         ROWS, COLS = len(grid), len(grid[0])

#         numberOfIslands = 0

#         def dfs(r: int, c: int) -> int:
#             #bounds or mismatch
#             if r < 0 or r >= ROWS or c < 0 or c >= COLS:
#                 return

#             # choose: mark visited
#             tmp = grid[r][c]
#             val = tmp
#             grid[r][c] = "#"  # any sentinel not in 'A'..'Z'


#             # explore neighbors (up, down, left, right)
            
#             if (dfs(r+1, c) == val or
#                 dfs(r-1, c) == val or
#                 dfs(r, c+1) == val or
#                 dfs(r, c-1) == val):

            
#                 return True
            

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1" and dfs(r, c):
#                     numberOfIslands += 1 


#         return numberOfIslands
    


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# output = 1

sol = Solution()

answer = sol.numIslands(grid)

print("answer", answer)