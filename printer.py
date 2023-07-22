from typing import List
import os


BOARD_INDENT = "    "
PLAYER_TO_TOKEN = {
    0: " ",
    1: "X",
    2: "O",
}
POSITION_TO_INDEXES = {
    1: (0, 0),  # (row, col)
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


def clear_screen():
    # os.system('cls' if os.name=='nt' else 'clear')
    print("\033c", end="")



def render_board(board: List[List[int]]):
    print("")
    print(BOARD_INDENT + " {0} | {1} | {2} ".format(
            PLAYER_TO_TOKEN[board[0][0]],
            PLAYER_TO_TOKEN[board[0][1]],
            PLAYER_TO_TOKEN[board[0][2]]))
    print(BOARD_INDENT + "---+---+---")
    print(BOARD_INDENT + " {0} | {1} | {2} ".format(
            PLAYER_TO_TOKEN[board[1][0]],
            PLAYER_TO_TOKEN[board[1][1]],
            PLAYER_TO_TOKEN[board[1][2]]))
    print(BOARD_INDENT + "---+---+---")
    print(BOARD_INDENT + " {0} | {1} | {2} ".format(
            PLAYER_TO_TOKEN[board[2][0]],
            PLAYER_TO_TOKEN[board[2][1]],
            PLAYER_TO_TOKEN[board[2][2]]))
    print("")


def render_instructions():
    print("Pick a position (1 through 9) and press [Enter] to play it.")
    print("Enter [q] to quit")


def render_end(board: List[List[int]]):
    clear_screen()
    render_board(board)
    

def render(board: List[List[int]]):
    clear_screen()
    render_board(board)
    render_instructions()

