class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = set()
        
        def dfs(i, j):
            visited.add((i, j))
            for di, dj in dirs:
                x = i + di
                y = j + dj
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == "1" and (x, y) not in visited:
                        dfs(x, y)
            return 
        
        
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    
                    count += 1
                    dfs(row, col)
        return count
        
        
        