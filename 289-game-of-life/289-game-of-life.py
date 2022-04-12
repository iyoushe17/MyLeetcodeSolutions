class Solution:
    def check(self, board, i, j):
        rows = len(board)
        cols = len(board[0])
        
        dirs = [(0,1), (1,0), (-1, 0), (0, -1), (1,1), (-1, -1), (-1, 1), (1, -1)]
        
        dead, live = 0, 0
        for di, dj in dirs:
            if 0 <= i + di < rows and 0 <= j + dj < cols:
                # dead
                if board[i + di][j + dj] in [2, 0]:
                    dead += 1
                # live
                if board[i + di][j + dj] in [1, -1]:
                    live += 1
        return (dead, live)
        
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
            
        
        # create a new board
        rows = len(board)
        cols = len(board[0])
        
        
        
        for i in range(rows):
            for j in range(cols):
                dead, live = self.check(board, i, j)
                if board[i][j] == 0:
                    if live == 3:
                        # resurrected
                        board[i][j] = 2
                else:
                    if live < 2 or live > 3:
                        # killed
                        board[i][j] = -1
                        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0

                        
                
                