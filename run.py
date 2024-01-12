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

