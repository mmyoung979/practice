"""
Simple Python battleship game
There is 1 ship on one square in a 3x3 board.
You have 3 guesses to figure out its location.
Good luck!
"""
# Python imports
from random import randint
from typing import List

# Global variables
SIZE = 3
WIN_MESSAGE = "You win!"
ERR_MESSAGE = f"value must be between 0 and {SIZE - 1}"


def create_board() -> List[List[str]]:
    """Initialize game board"""
    board = []
    for _ in range(SIZE):
        row = []
        for _ in range(SIZE):
            row.append("O")
        board.append(row)
    return board


def print_board(board) -> None:
    """Print current game board"""
    for row in board:
        print(row)


def place_ship() -> List[int]:
    """Create random location for ship"""
    x = randint(0, SIZE - 1)
    y = randint(0, SIZE - 1)
    return [x, y]


def make_guess(board, x, y, ship) -> List[List[str]]:
    """
    Check user guess for battleship location
    
    :param board: Current game board
    :param x: X-coordinate of guess
    :param y: Y-coordinate of guess
    :param ship: Battleship coordinates
    :returns: Updated game board
    """
    if [x, y] != ship:
        board[x][y] = "X"
        return board
    return WIN_MESSAGE


def play_again():
    """Ask player if they would like to play again"""
    interested = input("Would you like to play again? (yes/no)\n")
    if interested.lower() == "yes":
        interested = True
    elif interested.lower() == "no":
        interested = False
    else:
        return play_again()

    return interested


def main() -> None:
    """Play battleship game"""
    print("Welcome!")
    board = create_board()
    ship = place_ship()

    guesses_remaining = 3
    while guesses_remaining:
        print(f"\nYou have {guesses_remaining} guesses remaining.\n")

        x = int(input("x coordinate: "))
        while x < 0 or x > SIZE - 1:
            print(ERR_MESSAGE)
            x = int(input("x coordinate: "))

        y = int(input("y coordinate: "))
        while y < 0 or y > SIZE - 1:
            print(ERR_MESSAGE)
            y = int(input("y coordinate: "))

        board = make_guess(board, x, y, ship)
        if board == WIN_MESSAGE:
            print(board)
            break

        print_board(board)
        guesses_remaining -= 1

    print(f"The ship was located at {ship}")


    another_round = play_again()
    if another_round:
        main()
    else:
        print("Have a great day!")


if __name__ == "__main__":
    main()
