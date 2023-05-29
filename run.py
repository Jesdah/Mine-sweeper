import random
import pyfiglet
from colorama import Fore, Back, Style

# Declair some variables
top_row = Fore.BLUE + '1_______2_______3_______4_______5_______6' + Style.RESET_ALL
BOMB = Back.RED + "X" + Style.RESET_ALL
result = pyfiglet.figlet_format("Mine Sweeper")

score = 0


def minesweeper_heading():
    """
    Let the user start the game or read the instructions.
    If the user inputs the wrong inputs the function raises an Error.
    """
    print(result)  # Says MineSweeper.
    while True:
        try:
            start_instructions = input("Press 1 to start game\n"
                                       "Press 2 for instructions:\n")
            if start_instructions == "1":
                print(top_row)  # Starts the game
                break
            # Displayes the instuctions and then continue the loop
            if start_instructions == "2":
                print("Minesweeper is a game where mines "
                      "are hidden in a grid of squares.")
                print("Safe squares have numbers telling you "
                      "how many mines touch the square.")
                print("You can use the number clues to solve the game "
                      "by opening all of the safe squares.")
                print("If you click on a mine you lose the game!")
                continue
        except NameError as e:  # Ops something wrong
            print(Back.RED + "You must enter '1'"
                  f"or '2'. You entered:{e}" + Style.RESET_ALL)
        else:
            print(Back.RED + f"You must enter '1' or"
                  f"'2'. You entered:{start_instructions}" + Style.RESET_ALL)
    return False


def minesweeper(n):
    """
    This code was taken from:
    https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    Builds a game board 6*6 and randomly places a bomb
    and the neighbouring cells increase by +1.
    """

    arr = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    # for x in range(7):  # Generates "X" AKA Bombs
    x = random.randint(0, n-1)
    y = random.randint(0, n-1)
    arr[y][x] = BOMB

# Logic for the offsets.
    if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-1):
        if arr[y][x+1] != BOMB:
            arr[y][x+1] += 1  # center right
    if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-1):
        if arr[y][x-1] != BOMB:
            arr[y][x-1] += 1  # center left
    if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
        if arr[y-1][x-1] != BOMB:
            arr[y-1][x-1] += 1  # top left

    if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
        if arr[y-1][x+1] != BOMB:
            arr[y-1][x+1] += 1  # top right
    if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
        if arr[y-1][x] != BOMB:
            arr[y-1][x] += 1  # top center

    if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-2):
        if arr[y+1][x+1] != BOMB:
            arr[y+1][x+1] += 1  # bottom right
    if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
        if arr[y+1][x-1] != BOMB:
            arr[y+1][x-1] += 1  # bottom left
    if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
        if arr[y+1][x] != BOMB:
            arr[y+1][x] += 1  # bottom center

    return arr


def player_board():
    """
    Hides the real values from the player.
    """
    # This is what the player sees
    arr = [
        ["?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?"],
        ["?", "?", "?", "?", "?", "?"],
    ]

    return arr


def reviel_board(map):
    """
    Reviels the map when called.
    This code is from:
     https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    """

    for row in map:
        print("\t".join(str(cell) for cell in row))
        print("------------------------------------------")


def player_choise():
    """
    Allows the user to select coordinates on the board
    to open cells.
    """
    hidden_board = minesweeper(6)
    player_check = player_board()
    while True:
        global score  # scoreboard

        try:
            reviel_board(player_check)  # The player inputs thier guess
            print(Back.BLUE + "Enter your cell "
                  "you want to open: " + Style.RESET_ALL)
            player_first = input("X: Enter numbers 1-6: \n")
            player_second = input("Y: Enter numbers 1-6: \n")
            player_first = int(player_first) - 1  # input "1"=0
            player_second = int(player_second) - 1

        except ValueError:  # Oops!
            print(Back.RED + "Please enter a number "
                  "between 1-6." + Style.RESET_ALL)
            print(top_row)
            continue

# Assign player input to var "X" or "Y" to be checked below
        if player_first <= 5 and player_second <= 5:
            y = player_first
            x =  player_second

# Checks if hiddenboard and playercheck is equal, if it  is an error is raised
            if hidden_board[x][y] == player_check[x][y]:
                print(f"Score: {score}")  # Dislpays scoreboard
                print(Back.RED + "These coordinates have "
                      "already been used, try again!" + Style.RESET_ALL)
                print(top_row)
                continue

                # Checks if the user dug a bomb or not
            if hidden_board[x][y] != BOMB:
                player_check[x][y] = hidden_board[x][y]
                score += 1  # You got a point!
                print(f"Score: {score}")  # Dislpays scoreboard

# The user dug a bomb
            if hidden_board[x][y] == BOMB:
                print(f"Score: {score}")  # Dislpays scoreboard
                print(top_row)
                reviel_board(hidden_board)  # Reviels the board
                print(Back.RED + "Game over!" + Style.RESET_ALL)  # ohno!
                restart()

                # Checks if the user has reached the score of 28
            if score == 28:
                print(Back.GREEN + "You won!!" + Style.RESET_ALL)
                print(f"Score: {score}")
                restart()  # Calls the restart function

        else:
            print(Back.RED + "Please enter a number between 1-6. "
                  f"You entered:{player_first + 1} "
                  f"and {player_second + 1}." + Style.RESET_ALL)
        print(top_row)

    return False


def restart():
    """
    Allows the user to restart the game
    """
    while True:
        restart_game = input("Restart? Y/N:\n").lower()  # Yes or no?

# if yes
        if restart_game == "y":
            global score
            score = 0  # Score is set to 0
            main()  # main function is called

            # if no
        if restart_game == "n":
            print("Exit program.")
            exit()  # Exit program

        # Error message
        else:
            print(f"Please answer Yes or No (y/n), You entered:{restart_game}")
    return False


def main():
    """
    Runs all functions.
    """
    minesweeper_heading()
    minesweeper(6)
    player_board()
    player_choise()


main()
