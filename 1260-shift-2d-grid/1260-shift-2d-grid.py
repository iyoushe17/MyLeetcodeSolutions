class Solution:
    
        
        
    
    def shiftGrid(self, grid: List[List[int]], steps: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        newGrid = [[None for j in range(cols)] for i in range(rows)]
        
        
        
        
        for i in range(rows):
            
            for j in range(cols):
                newCol = (j + steps) % cols
                newRow = (i + ((j + steps) // cols)) % rows
                newGrid[newRow][newCol] = grid[i][j]
                
               
                
        
        return newGrid