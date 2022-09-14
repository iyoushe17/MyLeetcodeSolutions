'''
Change the 1s to 0s
If you don't want to change then add it to a visited data structure.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()
        
        def dfs(row, col):
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            ans = 1
            for dr, dc in dirs:
                x = row + dr
                y = col + dc
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y]:
                        ans += dfs(x, y)
            return ans
            
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    maxArea = max(maxArea, dfs(i, j))
                    
                    
        return maxArea