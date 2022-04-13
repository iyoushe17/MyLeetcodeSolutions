class Solution:
    
        
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[None for j in range(n)] for i in range(n)]
        
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        num = 1
        
        while left <= right and top <= bottom:
            
            # fill top row
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            top += 1
            
            # fill right vertical
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # fill bottom row
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
            
            # fill left vertical
        
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
                
            left += 1
            
        
        return matrix
        
        
        
        
        