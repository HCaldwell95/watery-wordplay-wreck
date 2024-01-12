# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def clear_terminal():
    """
    Clears the terminal ready for new content - https://www.geeksforgeeks.org/clear-screen-python/
    """
    os.system("cls" if os.name == "nt" else "clear")

def welcome_page():
    """
    Displays the main title page
    Prompts the player to press ENTER to begin the game
    """

    print("PLACEHOLDER FOR ASCII ART 'WATERY WORDPLAY WRECK'")
    print("PLACEHOLDER FOR 'Welcome to the Watery Wordplay Wreck!'")

    input("Please press ENTER to begin!\n")
    clear_terminal()
    game_introduction()

def game_rules():
    """
    Introduces the game and provides the user with the game rules
    """
    # Title
    print("PLACEHOLDER FOR ASCII ART 'RULES'")

    # Introduction to the game
    print("\nWelcome to Watery Wordplay Wreck!")
    print("Prepare to embark on a nautical journey of linguistic challenges.")
    print("In this game, you'll be deciphering words related to the sea.")
    print("Let's dive in!")

    # Line by line rules of the game
    print("\nRules of the Game:")
    print("1. Your first challenge is to guess a 3-letter word.")
    print("2. Successfully guessing a word advances you to the next level.")
    print("3. Each new level increases the word length by one letter, up to a maximum of 9 letters.")
    print("4. Keep guessing words until you reach the maximum length or make too many incorrect guesses.")
    print("5. The ship will stay afloat as long as you keep the words afloat in your mind!")

    print("\nAre you ready to set sail on this wordplay adventure? Let's begin!\n")

    # main()