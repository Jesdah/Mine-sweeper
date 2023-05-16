import math  
import random  
import pygame 

def minesweeper(n):
    """
    This code was taken from:
    https://medium.com/swlh/this-is-how-to-create-a-simple-minesweeper-game-in-python-af02077a8de
    Builds a game board 10*10 and randomly places a bomb
    and the neighbouring cells increase by +1.
    """
    arr = [[0 for row in range(n)] for column in range(n)]
    x = random.randint(0,8)
    y = random.randint(0,8)
    arr[y][x] = 'X'
    if (x >= 1 and x <= 10):
        arr[y][x+1] += 1 # center right
        arr[y][x-1] += 1 # center left
    if (x == 0):
        arr[y][x+1] += 1 # center right
    if (x == 4):
        arr[y][x-1] += 1 # center left
    if (x >= 1 and x <= 9) and (y >= 1 and y <= 9):
        arr[y-1][x-1] += 1 # top left
 
    if (x >= 0 and x <= 8) and (y >= 1 and y <= 9):
        arr[y-1][x+1] += 1 # top right
    if (x >= 0 and x <= 8) and (y >= 1 and y <= 9):
        arr[y-1][x] += 1 # top center
 
    if (x >=0 and x <= 8) and (y >= 0 and y <= 8):
        arr[y+1][x+1] += 1 # bottom right
    
    if (x >= 1 and x <= 9) and (y >= 0 and y <= 8):
        arr[y+1][x-1] += 1 # bottom left
    if (x >= 0 and x <= 8) and (y >= 0 and y <= 8):
        arr[y+1][x] += 1 # bottom center
    for row in arr:
        print(" ".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    minesweeper(10)
print(minesweeper)