def draw_sinking_ship(max_attempts):
    """
    Draws a sinking ship to represent remaining lives
    """
    if max_attempts == 6:
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠙⢿⣏⣹⣷⣄⠀⢴⣿⣿⠃⠀⠀⠀⠀⢀⡀⠀⠀ ")
        print("⠀⠀⠀⠸⣦⡙⠻⣿⣿⣿⣿⣷⣄⠙⢿⣤⡿⢷⣄⠙⠃⠀⠀⠀⠀⣀⡈⠻⠂⠀")
        print("⠀⠀⠀⠀⠈⠻⣦⡈⠻⣿⣿⣿⣿⣷⣄⠙⢷⣾⠛⣷⣄⠀⠀⢀⣴⣿⣿⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠻⣦⡈⠛⠛⠻⣿⣿⣷⣄⠙⠛⠋⢹⣷⣄⠈⠻⠛⠃⠀⠀⠀")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")

    elif max_attempts == 5:
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠙⢿⣏⣹⣷⣄⠀⢴⣿⣿⠃⠀⠀⠀⠀⢀⡀⠀⠀ ")
        print("⠀⠀⠀⠸⣦⡙⠻⣿⣿⣿⣿⣷⣄⠙⢿⣤⡿⢷⣄⠙⠃⠀⠀⠀⠀⣀⡈⠻⠂⠀")
        print("⠀⠀⠀⠀⠈⠻⣦⡈⠻⣿⣿⣿⣿⣷⣄⠙⢷⣾⠛⣷⣄⠀⠀⢀⣴⣿⣿⠀⠀⠀")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
    elif max_attempts == 4:
        print("                                        ")
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠙⢿⣏⣹⣷⣄⠀⢴⣿⣿⠃⠀⠀⠀⠀⢀⡀⠀⠀ ")
        print("⠀⠀⠀⠸⣦⡙⠻⣿⣿⣿⣿⣷⣄⠙⢿⣤⡿⢷⣄⠙⠃⠀⠀⠀⠀⣀⡈⠻⠂⠀")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
    elif max_attempts == 3:
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠙⢿⣏⣹⣷⣄⠀⢴⣿⣿⠃⠀⠀⠀⠀⢀⡀⠀⠀ ")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
    elif max_attempts == 2:
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⠀⠀⠈⣿⣿⣿⣷⣄⠙⢷⣾⠟⣷⣄⠀⠀⠀⠀⣠⣿⣦⠈⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
    elif max_attempts == 1:
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⣴⣄⠀⢀⣤⣶⣦⣀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ")
        print("⠀⠀⠀⢸⣿⣷⣌⠻⢿⣩⡿⢷⣄⠙⢿⠟⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀  ")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")
    elif max_attempts == 0:
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ")
        print("⠀⢀⣴⣿⣧⡀⠀⠀⠈⢁⣼⣿⣄⠙⢿⡿⠋⣠⣿⣧⡀⠠⡿⠗⢀⣼⣿⣦⡀⠀")
        print("⠀⠟⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⢷⣦⣴⡾⠛⠉⠙⠻⣶⣤⣶⠟⠋⠉⠛⠻⠀")
        print("⠀⣶⣿⣿⣿⣦⣄⣉⣠⣶⣿⣿⣷⣦⣈⣁⣴⣾⣿⣿⣶⣄⣉⣠⣶⣿⣿⣿⣶⠀")
        print("⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀")