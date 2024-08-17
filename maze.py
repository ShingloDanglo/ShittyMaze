import random
import os
import time
width, height = (31,31)
count = 0
matrix=[]
for row in range(width):
    a=[]
    for column in range(height):
        a.append(0)
    matrix.append(a)

startingX = random.randint(0,28)
startingY = random.randint(0,28)



def is_within_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def drawMaze():
    for i in range(height):
        for k in range(width):
            if (matrix[k][i]==1):
                printGap()
            else:
                printBlock()
        print("\n", end="")




def printBlock():
    print("██", end="")

def printGap():
    print("  ", end="")
    
def checkUp(x,y,lastDirection):
    if is_within_bounds(x, y-1) and is_within_bounds(x, y-2) and is_within_bounds(x-1, y-2) and is_within_bounds(x+1, y-2):
        print("up")
        if(matrix[x][y-1]!=1) and (matrix[x][y-2]==0) and (matrix[x-1][y-1]==0) and (matrix[x+1][y-1]==0):
            print("went up")
            nextCell(x,y-1, count, lastDirection)
                    
def checkDown(x,y,lastDirection):
    if y < height - 2 and is_within_bounds(x, y+1) and is_within_bounds(x, y+2) and is_within_bounds(x-1, y+2) and is_within_bounds(x+1, y+2):
        print("down")
        if(matrix[x][y+1]!=1) and (matrix[x][y+2]==0) and (matrix[x-1][y+1]==0) and (matrix[x+1][y+1]==0):
            print(" went down")
            nextCell(x,y+1, count,lastDirection)
            
def checkRight(x,y,lastDirection):
    if x < width - 2 and is_within_bounds(x+1, y) and is_within_bounds(x+2, y) and is_within_bounds(x+2, y-1) and is_within_bounds(x+2, y+1):
        print("right")
        if(matrix[x+1][y]!=1) and (matrix[x+2][y]==0) and (matrix[x+1][y-1]==0) and (matrix[x+1][y+1]==0):
            print(" went right")
            nextCell(x+1,y, count,lastDirection)
            
def checkLeft(x,y,lastDirection):
    if x > 1 and is_within_bounds(x-1, y) and is_within_bounds(x-2, y) and is_within_bounds(x-2, y-1) and is_within_bounds(x-2, y+1):
        print("left")
        if(matrix[x-1][y]!=1) and (matrix[x-2][y]==0) and (matrix[x-1][y-1]==0) and (matrix[x-1][y+1]==0):
            print(" went left")
            nextCell(x-1,y, count,lastDirection)
            
def randomCell(lastDirection):
    while True:
        newX = random.randint(0,width-1)
        newY = random.randint(0,height-1)
        if(matrix[newX][newY]==1):
            nextCell(newX, newY, count, lastDirection)
            break

def nextCell(x, y, count, lastDirection):
    matrix[x][y]=1
    
    count += 1
    if count > 50:
        drawMaze()
        return
    
    if(random.randint(1,2) == 1):
        direction = lastDirection
    else:
        direction = random.randint(1,101)
    
    if(direction >= 1) and (direction <= 25):
        checkUp(x,y, direction)
        checkRight(x,y, direction)
        checkDown(x,y, direction)
        checkLeft(x,y, direction)

                
    elif(direction >= 26) and (direction <= 50):
        checkRight(x,y, direction)
        checkDown(x,y, direction)
        checkLeft(x,y, direction)
        checkUp(x,y, direction)
                
    elif(direction >= 51) and (direction <= 75):
        checkDown(x,y, direction)
        checkLeft(x,y, direction)
        checkUp(x,y, direction)
        checkRight(x,y, direction)
                
    elif(direction >= 76) and (direction <= 100):
        checkLeft(x,y, direction)
        checkUp(x,y, direction)
        checkRight(x,y, direction)
        checkDown(x,y, direction)
    else:
        randomCell(direction)
            
 

nextCell(4, 5, count, 1)
drawMaze()