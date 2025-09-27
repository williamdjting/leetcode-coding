# answer 1 

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            # matched all characters
            if i == len(word):
                return True
            # bounds or mismatch
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i]:
                return False

            # choose: mark visited
            tmp = board[r][c]
            board[r][c] = "#"  # any sentinel not in 'A'..'Z'

            # explore neighbors (up, down, left, right)
            found = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )

            # un-choose: restore
            board[r][c] = tmp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


# solution 2
# from typing import List, Set, Tuple

# class SolutionVisited:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board or not board[0]:
#             return False

#         ROWS, COLS = len(board), len(board[0])
#         visited: Set[Tuple[int, int]] = set()

#         def dfs(r: int, c: int, i: int) -> bool:
#             if i == len(word):
#                 return True
#             if (r < 0 or r >= ROWS or
#                 c < 0 or c >= COLS or
#                 board[r][c] != word[i] or
#                 (r, c) in visited):
#                 return False

#             visited.add((r, c))
#             found = (
#                 dfs(r+1, c, i+1) or
#                 dfs(r-1, c, i+1) or
#                 dfs(r, c+1, i+1) or
#                 dfs(r, c-1, i+1)
#             )
#             visited.remove((r, c))
#             return found

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == word[0] and dfs(r, c, 0):
#                     return True
#         return False



# my attempt

# class Solution:
#     def exist(self, board: list[list[str]], word: str) -> bool:
#         """
#         Given an m x n grid of characters "board" and a string "word",
#         return True if the "word" exists in the grid.

#         The word can be constructed from letters of sequentially
#         adjacent cells, where adjacent cells are horizontally or
#         vertically neighboring. The same letter cell may not be
#         used more than once.
#         """
#         # logic, try to recreate the string 'word' inside 'board' by using dfs and backtracking to build 
#         # word in order form , S first, E second, E third (not duplicating)

#         wordArray : list[str] = []

#         for value in word:
#             wordArray.append(value)
        
#         # wordArray now contains ["S", "E" , "E" ]
#         # now I must search the neighbours of each node to find the value

#         results : list[str] = []

#         path = ""

#         def dfs(node, word, path):

#             if path == word:
#                 results.append(path)
#                 return
        
#             for neighbour in board[node]:
#                 if neighbour not in path: 
#                     path.append(neighbour)
#                     dfs(neighbour, path)
#                     path.pop()

#         dfs( "A", word, path)
#         return results


# sol = Solution()

# board = [["A","B","C","E"],
#         ["S","F","C","S"],
#         ["A","D","E","E"]]


# word = "SEE"

# answer = sol.exist(board, word)

# print("this is answer", answer)