class TicTacToeGame:

    def __init__(self):
        self.board = [[0] * 3] * 3

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

        row = (position - 1) // 3
        col = (position - 1) % 3
        
        if self.board[row][col] != 0:
            return False

        self.board[row][col] = player
        return True

