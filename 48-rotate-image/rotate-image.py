class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # problem can be divided into 2 steps:
        # step-1: first find the transpose of the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # step-2: in the second step reverse the rows back as for rotation only
        #         columns need to be reversed and rows can stay the same
        for rows in matrix:
            rows.reverse()