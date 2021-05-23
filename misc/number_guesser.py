"""
1. Display a welcome message
2. Generate a random number
3. Give the user 3 tries to guess the random number
4. Give the user the option to play again
"""
# Standard library imports
from random import randint


def play_number_guesser():
    """
    Generate a random number and give the user 3 tries
    to guess the random number.
    """
    # Display a welcome message
    welcome_message = "Guess a number between 1 and 10"
    print(welcome_message)

    # Generate a random number
    winning_number = randint(1, 10)

    # Give the user 3 tries to guess the random number
    tries_remaining = 3
    while tries_remaining > 0:
        print("-" * 30)

        # Make sure input is an integer
        try:
            guess = int(input("What is your guess?\n"))
        except ValueError:
            guess = 0

        if guess == winning_number:
            print("Congratulation! You win.")
            break
        elif guess < 1 or guess > 10:
            print("Remember! The number is between 1 and 10.")

        tries_remaining -= 1
        print("Sorry, that is not correct.")
        print(f"You have {tries_remaining} tries remaining.")

    # If the user's last guess was wrong
    if tries_remaining == 0:
        print("Game over.")
        print(f"The winning number was {winning_number}")

    # Give the user the option to play again
    play_again()


def play_again():
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again == "y":
        return play_number_guesser()
    elif play_again == "n":
        print("Have a great day!")
    else:
        print("Please enter y or n")
        return play_again()


if __name__ == "__main__":
    play_number_guesser()
