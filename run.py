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
    Prompts the user to press ENTER to begin the game
    Clears terminal before proceeding to next page
    """
    clear_terminal()

    print(ascii_art.GAME_TITLE)
    print(styles.BLUE_BOLD + "\nWelcome to the Watery Wordplay Wreck!" +
          styles.FIN)

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
          styles.FIN)
    print(styles.GREEN + "2. Suggest a word if you think you've got it!\n" +
          styles.FIN)

    print("\nChoose your difficulty by selecting the number of lives.")
    print("The ship will begin to sink after each incorrect guess.")
    print("I suggest we guess the word and save the ship before it sinks!")

    start_game()


def choose_num_of_lives():
    """
    Prompts the user to choose the number of lives for gameplay,
    enabling them to set the difficulty level.
    This loop persists until a valid input is submitted.
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
                  '" is not a valid option. Please try again.' + styles.FIN)


def get_random_word():
    """
    Pulls a random word from words.py for the user to guess.
    """
    return random.choice(sea_themed_words).upper()


def print_game_state(secret_word, used_letters, used_words, num_of_lives):
    """
    Prints the current state of the game.
    """
    if num_of_lives > 0:
        print(f"You have {num_of_lives} attempts left.\n")
    else:
        print("Game Over")

    print("\nYour " + styles.BOLD + str(len(secret_word)) +
          " LETTER " + styles.FIN + "word to guess is: " +
          secret_word)
    print(styles.BLUE + "Attempted letters: ",
          ", ".join(sorted(used_letters)) + styles.FIN)
    print(styles.BLUE + "Attempted words: ",
          ", ".join(sorted(used_words)) + styles.FIN)


def determine_game_outcome(secret_word, actual_word, num_of_lives):
    """
    Determines the game outcome and displays the appropriate message.
    """
    clear_terminal()

    if secret_word == actual_word:
        print("Congratulations!")
        print(f'"{actual_word}" was the correct answer!\n\n')
        draw_game_winner()
    else:
        print("Good effort! The correct word was " +
              f'"{actual_word}".')
        print("Thank you for playing our Watery Wordplay Wreck!\n")
        draw_game_over()


def restart_game():
    """
    Asks the user if they would like to play the game again.
    """

    while True:
        print("\nWould you like to play again? Enter " + styles.GRN_Y +
              " for " + styles.GRN_YES + " and  " + styles.RED_N +
              " for " + styles.RED_NO + "\n")

        restart_options = {"Y": game_rules, "N": welcome_page}

        restart = input("Please enter " + styles.GREEN + "Y " + styles.FIN +
                        "or " + styles.RED + "N" + styles.FIN + ":\n").upper()

        if restart in restart_options:
            clear_terminal()
            restart_options[restart]()
            break
        else:
            print(styles.YELLOW + 'Invalid Input: Please enter "Y" or "N".\n' +
                  styles.FIN)


def play_game(word, num_of_lives):
    """
    Plays the Watery Wordplay Wreck game.
    """
    secret_word = "_" * len(word)
    used_letters = []
    used_words = []

    clear_terminal()
    print("\nLet's play the Watery Wordplay Wreck! Good Luck.")
    print("\nThis word has " + styles.BLUE_BOLD + str(len(word)) +
          styles.FIN + " letters.")
    print("Good Luck!")

    draw_sinking_ship(num_of_lives)

    while num_of_lives > 0:
        guess = input(f"Please enter a {styles.BOLD}LETTER{styles.FIN} "
                      f"or a {styles.BOLD}WORD{styles.FIN}:\n").upper()
        clear_terminal()

        try:
            if not guess.isalpha():
                print(styles.YELLOW +
                      f'Invalid input: "{guess}" is not a valid letter.')
                print("Please enter a letter." + styles.FIN)

            elif len(guess) == len(word) and guess.isalpha():
                if guess in used_letters:
                    print(styles.YELLOW +
                          f"Invalid input: you have entered {len(guess)}" +
                          " letters.")
                    print("Please enter a letter " +
                          f"or word containing {len(word)} letters." +
                          styles.FIN)
                elif guess != word:
                    if guess not in used_words:
                        num_of_lives -= 1
                        used_words.append(guess)
                        print(styles.RED +
                              f'Sorry, "{guess}" is not the word.' +
                              styles.FIN)
                    else:
                        print(styles.YELLOW +
                              f'You have already tried "{guess}".')
                        print("Please try again!" + styles.FIN)
                else:
                    secret_word = word
                    break

            elif len(guess) != 1 or not guess.isalpha():
                print(styles.YELLOW +
                      f"Invalid input: you have entered {len(guess)} letters.")
                print("Please enter a letter " +
                      f"or word containing {len(word)} letters." + styles.FIN)

            elif guess in used_letters:
                print(styles.YELLOW + f'You have already tried "{guess}".')
                print("Please try again!" + styles.FIN)

            elif guess not in word:
                num_of_lives -= 1
                used_letters.append(guess)
                print(styles.RED +
                      f'Sorry, "{guess}" is not in the word.' + styles.FIN)
            else:
                used_letters.append(guess)
                print(styles.GREEN + f'"{guess}" IS in the word!')
                print("Good job!" + styles.FIN)

                word_as_list = list(secret_word)
                indices = [
                        i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                secret_word = "".join(word_as_list)
                if "_" not in secret_word:
                    break

        except ValueError as error:
            print(styles.YELLOW +
                  f'Invalid data: {error}, please try again.\n"' +
                  styles.FIN)
            continue

        print_game_state(secret_word, used_letters, used_words, num_of_lives)

        draw_sinking_ship(num_of_lives)

    determine_game_outcome(secret_word, word, num_of_lives)
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
