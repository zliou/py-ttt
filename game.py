BOARD_WIDTH = 3
BOARD_HEIGHT = 3


class TicTacToeGame:

    def __init__(self):
        self.board = [[0] * BOARD_WIDTH] * BOARD_HEIGHT

    """
    Attempt to place the given player's token at the given position.

    The board's positions are a 3x3 square, top-left to bottom right, starting from 1:
        123
        456
        789

    Returns a bool indicating whether the move was accepted.
    """
    def try_move(self, player: int, position: int) -> bool:
        # Validate player
        if player != 1 and player != 2:
            return False

        # Validate position
        if position < 1 or 9 < position:
            return False

        row = (position - 1) // BOARD_WIDTH
        col = (position - 1) % BOARD_HEIGHT
        
        if self.board[row][col] != 0:
            return False

        self.board[row][col] = player
        return True

    """
    Check the board for a win. Return the winning player id. 0 if no winner.
    """
    def check_win(self) -> int:
        # Check rows
        for row in range(BOARD_WIDTH):
            winner = self.check_row(row)
            if winner:
                return winner
        for col in range(BOARD_HEIGHT):
            winner = self.check_col(col)
            if winner:
                return winner
        return self.check_diagonals()

    def check_row(self, row: int) -> int:
        if (self.board[row][0] == 1 or self.board[row][0] == 2) and (
                self.board[row][0] == self.board[row][1] and 
                self.board[row][1] == self.board[row][2]):
            return self.board[row][0]
        return 0
        
    def check_col(self, col: int) -> int:
        if (self.board[0][col] == 1 or self.board[0][col]  == 2) and (
                self.board[0][col]  == self.board[1][col]  and 
                self.board[1][col]  == self.board[2][col] ):
            return self.board[0][col] 
        return 0

    def check_diagonals(self) -> int:
        if (self.board[0][0] == 1 or self.board[0][0] == 2) and (
                self.board[0][0] == self.board[1][1] and 
                self.board[1][1] == self.board[2][2]):
            return self.board[0][0]
        elif (self.board[2][0] == 1 or self.board[2][0] == 2) and (
                self.board[2][0] == self.board[1][1] and
                self.board[1][1] == self.board[0][2]):
            return self.board[2][0]
        else:
            return 0
            

        
        

