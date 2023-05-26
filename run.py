import math  
import random  
import pyfiglet
from colorama import Fore, Back, Style

result = pyfiglet.figlet_format("Mine Sweeper")
restart_minesweeeper = True
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
                print('1_______2_______3_______4_______5_______6')
                break
            if start_instructions=="2":
                print("Minesweeper is a game where mines are hidden in a grid of squares.\n"
                "Safe squares have numbers telling you how many mines touch the square.\n"
                "You can use the number clues to solve the game by opening all of the safe squares.\n"
                "If you click on a mine you lose the game!")
                continue
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
        x = random.randint(1,n-1)
        y = random.randint(1,n-1)
        arr[y][x] = 'X'
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
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
    
     
# def coordinates():
#     """
#     https://stackoverflow.com/questions/9989334/create-nice-column-output-in-python
#     """
#     numbers = ["1", "2", "3","4","5","6","7","8","9","10"] 
#     col_width = max(len(word) for row in numbers for word in row)  
#     for row in numbers:
#         print("".join(word.ljust(col_width) for word in row))

hidden_board=minesweeper(6,8)
player_check=player_board(6)
# user_coordinates=coordinates()
def player_choise():
    """
    Allows the user to select coordinates on the board
    to open cells.
    """
    # minesweeper(10,20)
    # player_board(10)
    while True:
        global score
        
    
        try:
            reviel_board(player_check)
            print("Enter your cell you want to open :")
            player_x= input("X: Enter numbers 1-6:")
            player_Y= input("Y: Enter numbers 1-6:")
            player_x=int(player_x) -1
            player_Y=int(player_Y) -1
    
        except ValueError:
            print("Please enter a number between 1-6.")
            print('1_______2_______3_______4_______5_______6')
            continue
            
        if player_x <=5 and player_Y <=5:
            # print("it works")
            x=player_x
            y=player_Y

            if hidden_board[x][y] == player_check[x][y]:
                print("These coordinates have already been used, try again!")
                continue

            if hidden_board[x][y]!="X":
                player_check[x][y] = hidden_board[x][y]
                # reviel_board(player_check)
                score += 1
                print(f"Score: {score}")
                # print('1_______2_______3_______4_______5_______6')
                
            if hidden_board[x][y]=="X":
                print('1_______2_______3_______4_______5_______6')
                reviel_board(hidden_board)
                print("Game over!")
                restart()
                
            if score == 28:
                print("You won!!")
                restart()
                       

        else: print(f"Please enter a number between 1-6. You entered:{player_x +1} and {player_Y +1}.")
        print('1_______2_______3_______4_______5_______6')
        
    return False


def restart():
    while True:
        restart_game = input("Restart? Y/N:")
                            
        if restart_game == "y":
            score=0
            main()
            print('yes!')

        if restart_game == "n":
            print("Exit program.")
            exit()

        else: print(f"Please answer Yes or No, You entered:{restart_game}")
    return False    

# if __name__ == "__main__":
#     try:
#         player_choise()
#     except KeyboardInterrupt:
#         print('\nEnd of Game. Bye Bye!')
     

def main():
    """
    Runs all functions.
    """
    score=0
    minesweeper_heading()
    minesweeper(6,8)
    player_board(6)
    
    player_choise()

main()
