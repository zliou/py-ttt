from typing import List


def clear_screen():
    print("\033c", end="")


def render_board():
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")


def render_instructions():
    print("Enter [x] to quit")


clear_screen()
render_board()

