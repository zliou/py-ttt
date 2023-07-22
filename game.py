import printer


BOARD_WIDTH = 3
BOARD_HEIGHT = 3
COMMAND_QUIT = "Q"
PLAYER_TO_TOKEN = {
    0: " ",
    1: "X",
    2: "O",
}


class TicTacToeGame:
    def __init__(self):
        self.board = []
        for i in range(BOARD_HEIGHT):
            row = []
            for j in range(BOARD_WIDTH):
                row.append(0)
            self.board.append(row)


    def get_player_input(self) -> str:
        return input()


    def is_valid_input(self, input_str) -> bool:
        return (len(input_str) == 1
                and (input_str <= "9" and input_str >= "1")
                or input_str == COMMAND_QUIT)


    """
    Play the game until a player wins, the board is full, or the quit command is received.
    """
    def play(self) -> None:
        active_player = 1  # Player 1 goes first.
        while not self.is_board_full():
            # Print the board before each move.
            printer.render(self.board)

            turn_result = self.turn(active_player)
            if turn_result == -1:
                print("{0} left the game.".format(PLAYER_TO_TOKEN[active_player]))
                print("Game over!")
                return
            elif turn_result != 0:
                # Reprint the board when someone wins.
                printer.render_end(self.board)
                print("{0} wins!".format(PLAYER_TO_TOKEN[active_player]))
                print("Thanks for playing!")
                return
            
            # Alternate turns between player 1 and 2.
            active_player = 2 if active_player == 1 else 1

        # Reprint the board before exiting from a tie.
        printer.render_end(self.board)

        print("It's a tie. Game over!")
        print("Thanks for playing!")
        return


    """
    Run a single turn of the game. Returns a winner if there is one, else 0.
    """
    def turn(self, player: int) -> int:
        print("It's {0}'s turn.".format(PLAYER_TO_TOKEN[player]))
        # Take player input until a player wins, the board is full, or the quit
        # command is issued.
        while True:
            position_input = self.get_player_input()
            if not self.is_valid_input(position_input):
                print("Invalid input.")
                continue
            if position_input == COMMAND_QUIT:
                return -1
            position = int(position_input)
            if self.try_move(player, position):
                break
            else:
                print("That spot is taken - try another spot.")
        return self.check_win()


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
    Return whether the board has no more open positions.
    """
    def is_board_full(self) -> bool:
        for row in self.board:
            for position in row:
                if position == 0:
                    return False
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
                self.board[0][col] == self.board[1][col]  and 
                self.board[1][col] == self.board[2][col]):
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
            
