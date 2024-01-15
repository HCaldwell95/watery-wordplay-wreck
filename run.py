# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Import random to allow words to be chosen randomly from words.py
import random
# Import os to interact with the native operating system to clear the terminal
import os

import ascii_art
from words import sea_themed_words
from sinking_ship import draw_sinking_ship


def clear_terminal():
    """
    Clears the terminal ready for new content
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_page():
    """
    Displays the main title page
    Prompts the player to press ENTER to begin the game
    """
    clear_terminal()

    print(ascii_art.TITLE)
    print("\nWelcome to the Watery Wordplay Wreck!")

    input("Please press ENTER to begin!\n")
    clear_terminal()
    game_rules()
    hangman()


def game_rules():
    """
    Introduces the game and provides the user with the game rules
    """

    clear_terminal()

    # Title
    print(ascii_art.RULES)

    # Line by line rules of the game
    print("\nRules of the Game:")
    print("1. Suggest one letter at a time to guess the word.")
    print("2. Successfully guessing a word advances you to the next level.")
    print("3. Each new level increases the word length by one letter.")
    print("4. Keep guessing words until you reach the maximum length or make ")
    print("   too many incorrect guesses.")

    print("\nYou will have 6 lives for each round.")
    print("The ship will begin to sink for each failed attempt")
    print("I suggest we guess the word and save the ship before it sinks!")

    print("\nYour first challenge is to guess a four-letter word.")

    input("\nPlease press ENTER when you are ready to set sail.\n")
    clear_terminal()


def get_random_word(word_length):
    filtered_words = [
            word for word in sea_themed_words if len(word) == word_length]
    return random.choice(filtered_words)


def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)


def hangman():

    print("Let's play the Watery Wordplay Wreck! Good Luck.")

    max_attempts = 6
    current_word_length = 4

    while current_word_length <= 9:
        word = get_random_word(current_word_length)
        guessed_letters = set()
        attempts = 0

        print(f"\nWord: {display_word(word, guessed_letters)} (length: {current_word_length})")

        while attempts < max_attempts:
            guess = input("Enter a letter: ").upper()

            if len(guess) == 1 and guess.isalpha():
                guessed_letters.add(guess)

                if all(letter.upper() in guessed_letters for letter in word):
                    print(f"Congratulations! You guessed the word: {word}")
                    current_word_length += 1
                    break

                if guess not in word:
                    attempts += 1
                    print(f"Incorrect guess! {max_attempts - attempts} attempts left.")
                else:
                    print(f"Good guess! Word: {display_word(word, guessed_letters)}")

            else:
                print(f'Invalid input: you have entered "{guess}"')
                print('Please enter a single letter.')
                continue

        else:
            print(f"\nGame Over! The word was {word}")
            current_word_length = 4  # Reset difficulty for the next round
            break

        draw_sinking_ship(max_attempts)


if __name__ == "__main__":
    welcome_page()
