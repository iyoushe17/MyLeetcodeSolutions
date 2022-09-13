class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cols = len(image[0])
        rows = len(image)
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        startColor = image[sr][sc]
        
        def flood(row, col):
            currentColor = image[row][col]
            if currentColor == startColor and currentColor != color:
                image[row][col] = color
                for di, dj in dirs:
                    if 0 <= row + di < rows and 0 <= col + dj < cols:
                        flood(row + di, col + dj)
            return
        
        flood(sr, sc)
        return image