# Import random to allow words to be chosen randomly from words.py
import random
# Import os to interact with the native operating system to clear the terminal
import os

import ascii_art
from words import sea_themed_words
from sinking_ship import draw_sinking_ship
from game_over import draw_game_over
from game_winner import draw_game_winner
from font_styles import styles


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
    print(styles.BLUEBOLD + "\nWelcome to the Watery Wordplay Wreck!" + styles.END)

    input("Please press ENTER to begin!\n")
    clear_terminal()
    game_rules()

    """
    while True:
        random_word, game_status = play_game(get_random_word(4))
        
        if game_status == "win":
            print("Congratulations! You won!")
        else:
            print("Thank you for playing our Watery Wordplay Wreck!")
        
        restart_game()
    """


def game_rules():
    """
    Introduces the game and provides the user with the game rules.
    """
    print(ascii_art.RULES)

    print("\nRules of the Game:")
    print(styles.GREEN + "1. Suggest one letter at a time to guess the word." + styles.END)
    print(styles.GREEN + "2. Suggest a word if you think you've cracked it!\n" + styles.END)

    print("\nBy selecting the number of lives, you will choose your difficulty.")
    print("The ship will begin to sink following each failed attempt.")
    print("I suggest we guess the word and save the ship before it sinks!")

    main()


def choose_num_of_lives():
    """
    Requests that the player selects the number of lives they 
    wish to play with, allowing them to set the difficulty. This
    loop continues until a valid input has been provided.
    """
    while True:
        print("\nPlease select the number of lives you wish to play with.")
        choice = input('Enter "4" for 4 lives, "6" for 6 lives or "8" for 8 lives:\n')

        if choice == "4":
            number_of_lives = 4
            return number_of_lives
        elif choice == "6":
            number_of_lives = 6
            return number_of_lives
        elif choice == "8":
            number_of_lives = 8
            return number_of_lives
        else:
            print(styles.YELLOW + f'Invalid input: you have entered "{choice}".')
            print('Please enter "4", "6", or "8".' + styles.END)


"""
If I can make incrementing difficulty work, use this:

def get_random_word(word_length):
    filtered_words = [
            word for word in sea_themed_words if len(word) == word_length]
    return random.choice(filtered_words)
"""
def get_random_word():
    """
    Pulls a random word from words.py for the player to guess.
    """
    word = random.choice(sea_themed_words)
    return word.upper()


"""
def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)
"""


def restart_game():
    """ 
    Asks the player if they would like to play the game again.
    """
    while True:
        print(f"\nWould you like to play again? Enter {styles.GREEN}Y{styles.END} for {styles.GREEN}YES{styles.END} and {styles.RED}N{styles.END} for {styles.RED}NO\n{styles.END}")
        restart = input(f"Please enter {styles.GREEN}Y{styles.END} or {styles.RED}N{styles.END}:\n").upper()
        if restart == "Y":
            clear_terminal()
            game_rules()
            break
        elif restart == "N":
            clear_terminal()
            welcome_page()
            break
        else: 
            print(styles.YELLOW + f'Invalid Input: Please enter "Y" or "N".\n' + styles.END)


def play_game(word, number_of_lives):
    used_letters = []
    secret_word = "_" * len(word)

    clear_terminal()
    print("\nLet's play the Watery Wordplay Wreck! Good Luck.")
    print("\nThis word has " + styles.BLUEBOLD + f"{len(word)} letters." + styles.END)
    print("Good Luck!")

    draw_sinking_ship(number_of_lives)

    while number_of_lives > 0:
        guess = input(f"Please enter a {styles.BOLD}LETTER {styles.END}or a {styles.BOLD}WORD{styles.END}:\n").upper()
        clear_terminal()
        try:
            if not guess.isalpha():
                print(styles.YELLOW + f'Invalid input: you have entered "{guess}".')
                print("Please enter a letter." + styles.END)

            elif len(guess) == len(word) and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW + f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)

                elif guess != word:
                    used_words.append(guess)
                    print(f'Sorry, "{guess}" is not the word.\n')
                    number_of_lives -= 1
                else:
                    secret_word = word
                    break

            elif len(guess) > 1 and guess.isalpha():
                print(styles.YELLOW + f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter "
                    f"or word containing {len(word)} letters." + styles.END)

            elif len(guess) == 1 and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW + f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)

                elif guess not in word:
                    number_of_lives -= 1
                    used_letters.append(guess)
                    print(styles.RED + f'Sorry, "{guess}" is not in the word.' + styles.END)
                    if number_of_lives > 0:
                        print(f"You have {number_of_lives} attempts left.")

                else:
                    used_letters.append(guess)
                    print(styles.GREEN + f'"{guess}" IS in the word!')
                    print("Good job!" + styles.END)

                    word_as_list = list(secret_word)
                    indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    secret_word = "".join(word_as_list)
                    if "_" not in secret_word:
                        break
            
        except ValueError as error:
            print(styles.YELLOW + f'Invalid data: {error}, please try again.\n"' + styles.END)
            continue

        if len(used_letters) <= 1 and number_of_lives > 0:
                print("\nThe word to guess: " + secret_word)
                print()

        elif number_of_lives > 0:
                print("\nThe word to guess: " + secret_word)
                print(styles.BLUE + "Attempted letters: ", ", ".join(sorted(used_letters)) + styles.END)
                
        draw_sinking_ship(number_of_lives)

    if secret_word == word:
        clear_terminal()
        print("Congratulations!")
        print(f'"{word}" was the correct answer!\n\n')
        draw_game_winner()

        """
        if current_word_length > MAX_WORD_LENGTH:
            print("You have beaten the game! Well done!")
        """
    else: 
        clear_terminal()
        print("Good effort! The correct word was " +
              f'"{word}".')
        print("Thank you for playing our Watery Wordplay Wreck!\n")
        draw_game_over()

    restart_game()

def main():
    """
    Calls the main functions to run the game
    """
    lives = choose_num_of_lives()
    random_word = get_random_word()
    play_game(random_word, lives)

welcome_page()