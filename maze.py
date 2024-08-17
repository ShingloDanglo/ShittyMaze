import random
import os
import time
width, height = (15,15)
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
    
def checkUp(x,y):
    if is_within_bounds(x, y-1) and is_within_bounds(x, y-2) and is_within_bounds(x-1, y-2) and is_within_bounds(x+1, y-2):
        print("up")
        if(matrix[x][y-1]!=1) and (matrix[x][y-2]==0) and (matrix[x-1][y-1]==0) and (matrix[x+1][y-1]==0):
            print("went up")
            nextCell(x,y-1, count)
                    
def checkDown(x,y):
    if y < height - 2 and is_within_bounds(x, y+1) and is_within_bounds(x, y+2) and is_within_bounds(x-1, y+2) and is_within_bounds(x+1, y+2):
        print("down")
        if(matrix[x][y+1]!=1) and (matrix[x][y+2]==0) and (matrix[x-1][y+1]==0) and (matrix[x+1][y+1]==0):
            print(" went down")
            nextCell(x,y+1, count)
            
def checkRight(x,y):
    if x < width - 2 and is_within_bounds(x+1, y) and is_within_bounds(x+2, y) and is_within_bounds(x+2, y-1) and is_within_bounds(x+2, y+1):
        print("right")
        if(matrix[x+1][y]!=1) and (matrix[x+2][y]==0) and (matrix[x+1][y-1]==0) and (matrix[x+1][y+1]==0):
            print(" went right")
            nextCell(x+1,y, count)
            
def checkLeft(x,y):
    if x > 1 and is_within_bounds(x-1, y) and is_within_bounds(x-2, y) and is_within_bounds(x-2, y-1) and is_within_bounds(x-2, y+1):
        print("left")
        if(matrix[x-1][y]!=1) and (matrix[x-2][y]==0) and (matrix[x-1][y-1]==0) and (matrix[x-1][y+1]==0):
            print(" went left")
            nextCell(x-1,y, count)
            

def nextCell(x, y, count):
    matrix[x][y]=1
    
    count += 1
    if count > 10:
        drawMaze()
        return
    
    direction = random.randint(1,101)
    
    if(direction >= 1) and (direction <= 25):
        checkUp(x,y)
        checkRight(x,y)
        checkDown(x,y)
        checkLeft(x,y)
                
    elif(direction >= 26) and (direction <= 50):
        checkRight(x,y)
        checkDown(x,y)
        checkLeft(x,y)
        checkUp(x,y)
                
    elif(direction >= 51) and (direction <= 75):
        checkDown(x,y)
        checkLeft(x,y)
        checkUp(x,y)
        checkRight(x,y)
                
    elif(direction >= 76) and (direction <= 100):
        checkLeft(x,y)
        checkUp(x,y)
        checkRight(x,y)
        checkDown(x,y)
    else:
        while True:
            newX = random.randint(0,width-1)
            newY = random.randint(0,height-1)
            if(matrix[newX][newY]==1):
                nextCell(newX, newY, count)
                break
            
 

nextCell(4, 5, count)
drawMaze()