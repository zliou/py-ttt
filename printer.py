from typing import List
import os


BOARD_INDENT = "    "
PLAYER_TO_TOKEN = {
    0: " ",
    1: "X",
    2: "O",
}
SUPERSCRIPT = {
    1: "¹", 2: "²", 3: "³",
    4: "⁴", 5: "⁵", 6: "⁶",
    7: "⁷", 8: "⁸", 9: "⁹",
}


def clear_screen():
    # os.system('cls' if os.name=='nt' else 'clear')
    print("\033c", end="")


def render_blank_row():
    print(BOARD_INDENT + "     |     |     ")


def render_player_row(row: List[int]):
    print(BOARD_INDENT + "  {0}  |  {1}  |  {2}  ".format(
            PLAYER_TO_TOKEN[row[0]],
            PLAYER_TO_TOKEN[row[1]],
            PLAYER_TO_TOKEN[row[2]]))


def render_position_row(start: int):
    print(BOARD_INDENT + "{0}    |{1}    |{2}    ".format(
            SUPERSCRIPT[start], SUPERSCRIPT[start + 1], SUPERSCRIPT[start + 2]))


def render_separator():
    print(BOARD_INDENT + "-----+-----+-----")


def render_board(board: List[List[int]]):
    print("")

    render_position_row(1)
    render_player_row(board[0])
    render_blank_row()

    render_separator()

    render_position_row(4)
    render_player_row(board[1])
    render_blank_row()

    render_separator()

    render_position_row(7)
    render_player_row(board[2])
    render_blank_row()

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

