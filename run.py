import math  
import random  
import pyfiglet
 
result = pyfiglet.figlet_format("Mine Sweeper")

def minesweeper_heading():
    """
    Let the user start the game or read the instructions.
    If the user inputs the wrong inputs the function raises an Error.
    """
    print(result)
    while True:
        try:
            start_instructions= input("Press 1 to start game\nPress 2 for instructions:")
            print(start_instructions)
            if start_instructions== "1":
                print("it works!")
                break
            if start_instructions=="2":
                print("Minesweeper is a game where mines are hidden in a grid of squares.\n"
                "Safe squares have numbers telling you how many mines touch the square.\n"
                "You can use the number clues to solve the game by opening all of the safe squares.\n"
                "If you click on a mine you lose the game!")
        except NameError as e:
            print(f"You must enter '1' or '2'. You entered:{e}")
        else: print(f"You must enter '1' or '2'. You entered:{start_instructions}")
    return False


def minesweeper(n,k):
    """
    This code was taken from:
    https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    Builds a game board 10*10 and randomly places a bomb
    and the neighbouring cells increase by +1.
    """

    arr = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= 8) and (y >= 0 and y <= 9):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= 9) and (y >= 0 and y <= 9):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center
    
    return arr


def player_board(n):
    """
    This code was copied from:
    https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    Hides the real values from the player.
    """
    arr = [["*" for row in range(n)] for column in range(n)]
    for row in arr:
        print("\t".join(str(cell) for cell in row))
        print("")
    return arr



def player_choise():
    """
    Allows the user to select coordinates on the board
    to open cells.
    """
    while True:
        print("Enter your cell you want to open :")
        player_x= input("X: Enter numbers 1-9:")
        player_Y= input("Y: Enter numbers 1-9:")
        player_x=int(player_x)
        player_Y=int(player_Y)
    
        try:
            if 0 < player_x <=9 and 0 < player_Y <=9:
                print("its working!!")
                player_x = x
                player_Y = y
                break
            else: print(f"Please enter a number between 1-9. You entered:{player_x} and {player_Y}.")
        except NameError as e:
            print(f"NameError{e}")
    return False

    if
    

    



def main():
    """
    Runs all functions.
    """
    minesweeper_heading()
    minesweeper(10,20)
    player_board(10)
    player_choise()

main()
print(main)