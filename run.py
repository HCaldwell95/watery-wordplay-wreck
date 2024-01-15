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
    random_word = get_random_word(4)
    play_game(random_word)


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

def restart_game():
    """ 
    Asks the player if they would like to play the game again.
    
    """




""" 
Testing Code to see if better than existing
"""

def play_game(word, max_attempts=6):
    current_word_length = len(word)
    used_letters = []
    used_words = []
    secret_word = "_" * len(word)

    clear_terminal()
    print("\nLet's play the Watery Wordplay Wreck! Good Luck.")
    print("\nThis word has " + f"{len(word)} letters.")
    print("Good Luck!")

    draw_sinking_ship(max_attempts)

    while max_attempts > 0:
        guess = input("Please enter a letter or a word:\n").upper()
        clear_terminal()
        try:

            if not guess.isalpha():
                print(f'Invalid input: you have entered "{guess}".')
                print("Please enter a letter.")
                continue

            elif len(guess) == len(word) and guess.isalpha():
                if guess in used_letters:
                    print(f'You have already tried "{guess}".')
                    print("Please try again!")

                elif guess != word:
                    used_words.append(guess)
                    print(f'Sorry, "{guess}" is not the word.\n')
                    max_attempts -= 1
                else:
                    secret_word = word
                    break

            elif len(guess) > 1 and guess.isalpha():
                print(f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter "
                      f"or word containing {len(word)} letters.")

            elif len(guess) == 1 and guess.isalpha():
                if guess in used_letters:
                    print(f'You have already tried "{guess}".')
                    print("Please try again!")
                elif guess not in word:
                    max_attempts -= 1
                    used_letters.append(guess)
                    print(f'Sorry, "{guess}" is not in the word.')
                    if max_attempts > 0:
                        print(f"You have {max_attempts} attempts left.")
                else:
                    used_letters.append(guess)
                    print(f'"{guess}" IS in the word!')
                    print("Good job!")

                    word_as_list = list(secret_word)
                    indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    secret_word = "".join(word_as_list)
                    if "_" not in secret_word:
                        break
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            continue

        if len(used_letters) <= 1 and max_attempts > 0:
            print("\nThe word to guess: " + secret_word)
            print()

        elif max_attempts > 0:
            print("\nThe word to guess: " + secret_word)
            print("Attempted letters: ", ", ".join(sorted(used_letters)))
        
        draw_sinking_ship(max_attempts)

    if secret_word == word:
        current_word_length += 1
        clear_terminal()
        print("Congratulations!")
        print(f'"{word}" was the correct answer!')
        
        
    
    else: 
        clear_terminal()
        print("Good effort! The correct word was " +
              f'"{word}"')
        print("Thank you for playing our Watery Wordplay Wreck!")

    restart_game()

def main():
    """
    Calls the main functions to run the game
    """
    clear_terminal()
    welcome_page()

main()