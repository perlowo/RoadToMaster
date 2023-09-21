from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        board = [[''] * n for _ in range(n)]
        
        for i, move in enumerate(moves):
            x, y = move
            if i % 2 == 0:
                board[x][y] = 'A'
            else:
                board[x][y] = 'B'
        
        def check_winner(player):
            for row in board:
                if all(cell == player for cell in row):
                    return True
            
            for col in range(n):
                if all(board[row][col] == player for row in range(n)):
                    return True
            
            if all(board[i][i] == player for i in range(n)) or all(board[i][n - i - 1] == player for i in range(n)):
                return True
            
            return False
        
        if check_winner('A'):
            return "A"
        if check_winner('B'):
            return "B"
        
        return "Draw" if len(moves) == n * n else "Pending"

moves = [[0, 0], [1, 1], [2, 2], [0, 2], [1, 0], [2, 1], [0, 1], [1, 0], [2, 1]]
solution = Solution()
result = solution.tictactoe(moves)
print(result)
