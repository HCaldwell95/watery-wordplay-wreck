# Import random to allow words to be chosen randomly from words.py
import random
# Import os to interact with the native operating system to clear the terminal
import os

# Import necessary local modules
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
    print(styles.BLUEBOLD + "\nWelcome to the Watery Wordplay Wreck!" +
          styles.END)

    input("Please press ENTER to begin!\n")
    clear_terminal()
    game_rules()


def game_rules():
    """
    Introduces the game and provides the user with the game rules.
    """
    print(ascii_art.RULES)

    print("\nRules of the Game:")
    print(styles.GREEN + "1. Suggest one letter at a time to guess the word." +
          styles.END)
    print(styles.GREEN + "2. Suggest a word if you think you've got it!\n" +
          styles.END)

    print("\nChoose your difficulty by selecting the number of lives.")
    print("The ship will begin to sink following each failed attempt.")
    print("I suggest we guess the word and save the ship before it sinks!")

    start_game()


def choose_num_of_lives():
    """
    Requests that the player selects the number of lives they wish to play
    with, allowing them to set the difficulty. This loop continues until a
    valid input has been provided.
    """
    options = {"8": "Easy", "6": "Medium", "4": "Hard"}

    while True:
        print("\nSelect the difficulty level by choosing the number of lives:")
        for option, difficulty in options.items():
            print(f'Enter "{option}" for {difficulty}')

        choice = input().strip()
        if choice in options:
            return int(choice)
        else:
            print(styles.YELLOW + 'Invalid input: "' + choice +
                  '" is not a valid option. Please try again.' + styles.END)


def get_random_word():
    """
    Pulls a random word from words.py for the player to guess.
    """
    word = random.choice(sea_themed_words)
    return word.upper()


def restart_game():
    """
    Asks the player if they would like to play the game again.
    """
    while True:
        print("\nWould you like to play again? Enter " + styles.GRN_Y +
              " for " + styles.GRN_YES + " and  " + styles.RED_N +
              " for " + styles.RED_NO + "\n")
        restart = input("Please enter " + styles.GREEN + "Y " + styles.END +
                        "or " + styles.RED + "N" + styles.END + ":\n").upper()
        if restart == "Y":
            clear_terminal()
            game_rules()
            break
        elif restart == "N":
            clear_terminal()
            welcome_page()
            break
        else:
            print(styles.YELLOW + 'Invalid Input: Please enter "Y" or "N".\n' +
                  styles.END)


def play_game(word, number_of_lives):
    """
    Performs the core functions of the game
    """
    
    # Displays the secret word to the user via underscores
    secret_word = "_" * len(word)

    used_letters = []
    used_words = []
    clear_terminal()
    print("\nLet's play the Watery Wordplay Wreck! Good Luck.")
    print("\nThis word has " + styles.BLUEBOLD + f"{len(word)} letters." +
          styles.END)
    print("Good Luck!")

    draw_sinking_ship(number_of_lives)

    # Main game loop
    while number_of_lives > 0:
        # Prompts the user for a letter or a word
        guess = input("Please enter a " + styles.BOLD + "LETTER " +
                      styles.END + "or a " + styles.BOLD + "WORD" +
                      styles.END + ":\n").upper()
        clear_terminal()
        try:
            # Checks if the input is not a letter
            if not guess.isalpha():
                print(styles.YELLOW +
                      f'Invalid input: you have entered "{guess}".')
                print("Please enter a letter." + styles.END)

            # Checks if the input is a word of the correct length
            elif len(guess) == len(word) and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW + f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)

                # Decreases number of lives and updates the use words list
                elif guess != word:
                    number_of_lives -= 1
                    used_words.append(guess)
                    print(styles.RED + f'Sorry, "{guess}" is not the word.' +
                          styles.END)
                    if number_of_lives > 0:
                        print(f"You have {number_of_lives} attempts left.")
                else:
                    secret_word = word
                    break

            # Checks if the input is a word of incorrect length
            elif len(guess) > 1 and guess.isalpha():
                print(styles.YELLOW +
                      f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter " +
                      f"or word containing {len(word)} letters." + styles.END)

            # Checks if the input is a single letter
            elif len(guess) == 1 and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW + f'You have already tried "{guess}".')
                    print("Please try again!" + styles.END)

                # Decrements lives, updates used letters and provides feedback
                elif guess not in word:
                    number_of_lives -= 1
                    used_letters.append(guess)
                    print(styles.RED +
                          f'Sorry, "{guess}" is not in the word.' + styles.END)
                    if number_of_lives > 0:
                        print(f"You have {number_of_lives} attempts left.")

                # Updates the secret word with the correct letters
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

        # Handles invalid data input
        except ValueError as error:
            print(styles.YELLOW +
                  f'Invalid data: {error}, please try again.\n"' +
                  styles.END)
            continue

        # Displays the current state of the game
        if len(used_letters) <= 1 and number_of_lives > 0:
            print("\nYour " + styles.BOLD + str(len(secret_word)) +
                  " LETTER " + styles.END + "word to guess is: " +
                  secret_word)
            print(styles.BLUE + "Attempted letters: ",
                  ", ".join(sorted(used_letters)) + styles.END)
            print(styles.BLUE + "Attempted words: ",
                  ", ".join(sorted(used_words)) + styles.END)

        elif number_of_lives > 0:
            print("\nYour " + styles.BOLD + str(len(secret_word)) +
                  " LETTER " + styles.END + "word to guess is: " +
                  secret_word)
            print(styles.BLUE + "Attempted letters: ",
                  ", ".join(sorted(used_letters)) + styles.END)
            print(styles.BLUE + "Attempted words: ",
                  ", ".join(sorted(used_words)) + styles.END)

        draw_sinking_ship(number_of_lives)

    # Determines the game outcome and displays the appropriate message
    if secret_word == word:
        clear_terminal()
        print("Congratulations!")
        print(f'"{word}" was the correct answer!\n\n')
        draw_game_winner()

    else:
        clear_terminal()
        print("Good effort! The correct word was " +
              f'"{word}".')
        print("Thank you for playing our Watery Wordplay Wreck!\n")
        draw_game_over()

    restart_game()


def start_game():
    """
    Initialises a new game of Watery Wordplay Wreck by setting up the game
    parameters, including the number of lives and selecting a random word
    to be guessed.
    """
    lives = choose_num_of_lives()
    random_word = get_random_word()
    play_game(random_word, lives)


# Starts the game when the script is executed
welcome_page()
