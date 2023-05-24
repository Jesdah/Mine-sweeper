import math  
import random  
import pyfiglet
 
result = pyfiglet.figlet_format("Mine Sweeper")
score = 0
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

    arr = [[1 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(1,n-1)
        y = random.randint(1,n-1)
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
    return arr

def reviel_board(map):
    """
    Reviels the map when called.
    This code is from:
     https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    """
    for row in map:
        print("\t".join(str(cell) for cell in row))
        print("")

def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '*':
                return False
    return True

hidden_board=minesweeper(10,20)
player_check=player_board(10)
def player_choise():
    """
    Allows the user to select coordinates on the board
    to open cells.
    """
    global score
    reviel_board(player_check)
    while True:
        try:
            print("Enter your cell you want to open :")
            player_x= input("X: Enter numbers 1-10:")
            player_Y= input("Y: Enter numbers 1-10:")
            player_x=int(player_x) -1
            player_Y=int(player_Y) -1
    
        except ValueError:
            print("Please enter a number between 1-10.")
            continue
            
        if player_x <=9 and player_Y <=9:
            print("its working!!")
            x=player_x
            y=player_Y

            if hidden_board[x][y] == player_check[x][y]:
                print("These coordinates have already been used, try again!")
                continue

            if hidden_board[x][y]!="X":
                player_check[x][y] = hidden_board[x][y]
                reviel_board(player_check)
                score += 1
                print(f"Score: {score}")
                print("its looking realy good")
                
            if hidden_board[x][y]=="X":
                reviel_board(hidden_board)
                print("Game over!")
                restart()
                
            if score == 20:
                print("You won!!")
                restart()
                       

        else: print(f"Please enter a number between 1-10. You entered:{player_x +1} and {player_Y +1}.")
        
    return False

    
def restart():
    while True:
        restart_game = input("Restart? Y/N:")
                            
        if restart_game == "y":
            main()

        if restart_game == "n":
            print("Exit program.")
            exit()

        else: print(f"Please answer Yes or No, You entered:{restart_game}")
    return False    

    
     

def main():
    """
    Runs all functions.
    """
    minesweeper_heading()
    
    
    player_choise()

main()
print(main)