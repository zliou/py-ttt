from typing import List


def clear_screen() -> None:
    print("\033c", end="")


def render_board() -> None:
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")


clear_screen()
render_board()

