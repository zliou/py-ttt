from typing import List

from game import TicTacToeGame


def test(results: List[bool], descriptions: List[str], result: bool, description: str):
    descriptions.append(description)
    results.append(result)


t, d = [], []


ttt = TicTacToeGame()


test(t, d, ttt.try_move(1, 1) == True,      "Valid move."),
test(t, d, ttt.try_move(1, 1) == False,     "Invalid move: position occupied."),
test(t, d, ttt.try_move(9, 2) == False,     "Invalid player id."),
test(t, d, ttt.try_move(2, 0) == False,     "Invalid position."),


all_tests_passed = True
for i in range(len(t)):
    if not t[i]:
        all_tests_passed = False

    result_str = "PASSED" if t[i] else "FAILED"
    print("[" + result_str + "]", d[i])

if all_tests_passed:
    print("All tests passed! :)")


