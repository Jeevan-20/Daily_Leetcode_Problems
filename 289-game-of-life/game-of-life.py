from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])  
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(rows):
            for j in range(cols):
                live_neighbors = sum(
                    1 for dx, dy in directions
                    if 0 <= i + dx < rows and 0 <= j + dy < cols and board[i + dx][j + dy]  in [1, 2]
                )
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2 
                elif board[i][j] == 0:  
                    if live_neighbors == 3:
                        board[i][j] = 3  
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0  
                elif board[i][j] == 3:
                    board[i][j] = 1  
