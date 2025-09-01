class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #  matrix = 
        # [[1,2,3],
        # [4,5,6],
        # [7,8,9]]
        # rotate 90 degrees clock wise it should become
        # rotatedMatrix = 
        # [[7,4,1],
        # [8,5,2],
        # [9,6,3]]
        # do this in place

        # the pattern is 
        # 1 @ 0,0 becomes 0,0 then reverse = 0,2 = moving 2 increments
        # 4 @ 1,0 becomes 0,1 then reverse = 0,1
        # 6 @ 1,2 becomes 2,1 then reverse = 2,1
        # 8 @ 2,1 becomes 1,2 then reverse = 1,0

        # rows, cols = len(matrix), len(matrix[0])

        # for i in range(rows):         # row index
        #     for j in range(cols):     # column index
        #         print(f"matrix[{i}][{j}] = {matrix[i][j]}")

        # in place solution, transpose swap row, col to col, row
        n = len(matrix)
        # transpose via upper triangle
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for i in range(n):
            matrix[i].reverse()



sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol.rotate(matrix)

print("done, no return")