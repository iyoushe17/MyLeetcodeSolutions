class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        total = len(matrix)
        
        for row in range(total):
            for col in range(row + 1, total):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(total):
            for col in range(total//2):
                matrix[row][col], matrix[row][total - col - 1] = matrix[row][total - col - 1], matrix[row][col]
        
        
            