class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Given an m x n grid of characters board and a string word,
        return True if the word exists in the grid.

        The word can be constructed from letters of sequentially
        adjacent cells, where adjacent cells are horizontally or
        vertically neighboring. The same letter cell may not be
        used more than once.
        """
        



sol = Solution()

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 

word = "SEE"

answer = sol.exist(board, word)

print("this is answer", answer)