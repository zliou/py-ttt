"""
File: game_test.py
Date: 2023 July 22

To run these tests, run the command:
    $ python3 game_test.py
"""
from typing import List

from game import TicTacToeGame


# Define test utilities.
def test(results: List[bool], descriptions: List[str], result: bool, description: str):
    descriptions.append(description)
    results.append(result)

t, d = [], []
ttt = TicTacToeGame()


# -------------------------------------------------------------------
# Run tests.
# NOTE: The tests below may be order-dependent.


# Try-move tests.
test(t, d, ttt.try_move(1, 1) == True,      "try_move: Valid move.")
test(t, d, ttt.try_move(1, 1) == False,     "try_move: Invalid move: position occupied.")
test(t, d, ttt.try_move(9, 2) == False,     "try_move: Invalid player id.")
test(t, d, ttt.try_move(2, 0) == False,     "try_move: Invalid position.")


# Board tests.
ttt.board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
test(t, d, ttt.is_board_full() == False,    "is_board_full: Board is not full.")
ttt.board = [
    [1,2,1],
    [2,2,1],
    [2,1,2],
]
test(t, d, ttt.is_board_full() == True,     "is_board_full: Board is full.")


# Win checking tests.
ttt.board = [
    [1,1,1],
    [0,2,0],
    [0,2,0],
]
test(t, d, ttt.check_win() == 1,            "check_win: Valid win with row.")
test(t, d, ttt.check_row(0) == 1,           "check_row: Winning row.")
test(t, d, ttt.check_row(1) == 0,           "check_row: Not a winning row.")
ttt.board = [
    [1,2,1],
    [0,2,0],
    [0,2,0],
]
test(t, d, ttt.check_win() == 2,            "check_win: Valid win with col.")
test(t, d, ttt.check_col(1) == 2,           "check_col: Winning col.")
test(t, d, ttt.check_col(2) == 0,           "check_col: Not a winning col.")
test(t, d, ttt.check_diagonals() == 0,      "check_diagonals: No winning diagonals.")
ttt.board = [
    [1,1,2],
    [0,2,0],
    [2,1,0],
]
test(t, d, ttt.check_diagonals() == 2,      "check_diagonals: Winning diagonal: BL-TR.")
ttt.board = [
    [1,1,2],
    [0,1,0],
    [2,2,1],
]
test(t, d, ttt.check_diagonals() == 1,      "check_diagonals: Winning diagonal: TL-BR.")
test(t, d, ttt.check_win() == 1,            "check_win: Valid win with diagonal.")


# Input tests.
test(t, d, ttt.is_valid_input("1"),         "is_valid_input: Valid input.")
test(t, d, ttt.is_valid_input("0") == False,"is_valid_input: Invalid input.")
test(t, d, ttt.is_valid_input("q"),         "is_valid_input: Quit command.")
# test(t, d, ttt.get_player_input() == "3",   "get_player_input: Player inputs '3'")


# Turn tests.
ttt.board = [
    [0,0,0],
    [0,1,0],
    [2,2,0],
]

ttt.get_player_input = lambda: "3"  # Mock get_player_input
test(t, d, ttt.turn(1) == 0,                "turn: Turn with valid position.")
# test(t, d, ttt.turn(2) == 0,                "turn: Turn with invalid position.")
ttt.get_player_input = lambda: "9"  # Mock get_player_input
test(t, d, ttt.turn(2) == 2,                "turn: Turn with valid position resulting in P2 win.")
ttt.get_player_input = lambda: "q"  # Mock get_player_input
test(t, d, ttt.turn(2) == -1,               "turn: Turn with quit command.")


# -------------------------------------------------------------------


# Run tests.
all_tests_passed = True
for i in range(len(t)):
    if not t[i]:
        all_tests_passed = False

    result_str = "--[PASS]" if t[i] else "[FAILED]"
    print(result_str, d[i])

if all_tests_passed:
    print("game_test.py: All tests passed! :)")
else:
    print("game_test.py: Some tests did not pass. See above for details.")
print("")

