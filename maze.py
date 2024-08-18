import random
import os
import time
width = 65
height = 65
count = 0
matrix=[]
for row in range(width):
    a=[]
    for column in range(height):
        a.append(0)
    matrix.append(a)

startingX = random.randint(1,width-2)
startingY = random.randint(0,0)



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
    
def checkUp(x,y,count,lastDirection):
    if y > 1 and is_within_bounds(x, y-1) and is_within_bounds(x, y-2) and is_within_bounds(x-1, y-2) and is_within_bounds(x+1, y-2):
        #print("up")
        if(matrix[x][y-1]!=1) and (matrix[x][y-2]==0) and (matrix[x-1][y-1]==0) and (matrix[x+1][y-1]==0) and (matrix[x-1][y-2]==0) and (matrix[x+1][y-2]==0):
            #print("went up")
            nextCell(x,y-1, count, lastDirection)
                    
def checkDown(x,y,count,lastDirection):
    if y < height - 2 and is_within_bounds(x, y+1) and is_within_bounds(x, y+2) and is_within_bounds(x-1, y+2) and is_within_bounds(x+1, y+2):
        #print("down")
        if(matrix[x][y+1]!=1) and (matrix[x][y+2]==0) and (matrix[x-1][y+1]==0) and (matrix[x+1][y+1]==0) and (matrix[x-1][y+2]==0) and (matrix[x+1][y+2]==0):
            #print(" went down")
            nextCell(x,y+1, count,lastDirection)
            
def checkRight(x,y,count,lastDirection):
    if x < width - 2 and is_within_bounds(x+1, y) and is_within_bounds(x+2, y) and is_within_bounds(x+2, y-1) and is_within_bounds(x+2, y+1):
        #print("right")
        if(matrix[x+1][y]!=1) and (matrix[x+2][y]==0) and (matrix[x+1][y-1]==0) and (matrix[x+1][y+1]==0) and (matrix[x+2][y-1]==0) and (matrix[x+2][y+1]==0):
            #print(" went right")
            nextCell(x+1,y, count,lastDirection)
            
def checkLeft(x,y,count,lastDirection):
    if x > 1 and is_within_bounds(x-1, y) and is_within_bounds(x-2, y) and is_within_bounds(x-2, y-1) and is_within_bounds(x-2, y+1):
        #print("left")
        if(matrix[x-1][y]!=1) and (matrix[x-2][y]==0) and (matrix[x-1][y-1]==0) and (matrix[x-1][y+1]==0) and (matrix[x-2][y-1]==0) and (matrix[x-2][y+1]==0):
            #print(" went left")
            nextCell(x-1,y, count,lastDirection)
            
def randomCell(count,lastDirection):
    while True:
        newX = random.randint(0,width-1)
        newY = random.randint(0,height-1)
        if(matrix[newX][newY]==1):
            nextCell(newX, newY, count, lastDirection)
            break

def selectEndpoint():
    possibleEndings=[]
    for cell in range(width):
        if(matrix[cell][height-2]==1):
            possibleEndings.append(cell)
            
    matrix[random.choice(possibleEndings)][height-1]=1
            

#nextCell recursively generates maze
def nextCell(x, y, count, lastDirection):
    matrix[x][y]=1
    #drawMaze()
    """for cell in range(width):
        if (matrix[cell][height-1]==1) or (matrix[cell][0]==1):
            print("Uh oh")
            return"""
    
    count += 1
    print(count)
    if count > (width+height)/2:
        #drawMaze()
        return
    
    if(random.randint(1,2) == 1):
        direction = lastDirection
    else:
        direction = random.randint(1,101)
    
    if(direction >= 1) and (direction <= 25):
        checkUp(x,y, count, direction)
        checkRight(x,y, count, direction)
        checkDown(x,y, count, direction)
        checkLeft(x,y, count, direction)
        randomCell(count,direction)

                
    elif(direction >= 26) and (direction <= 50):
        checkRight(x,y, count, direction)
        checkDown(x,y, count, direction)
        checkLeft(x,y, count, direction)
        checkUp(x,y, count, direction)
        randomCell(count,direction)
                
    elif(direction >= 51) and (direction <= 75):
        checkDown(x,y, count, direction)
        checkLeft(x,y, count, direction)
        checkUp(x,y, count, direction)
        checkRight(x,y, count, direction)
        randomCell(count,direction)
                
    elif(direction >= 76) and (direction <= 100):
        checkLeft(x,y, count, direction)
        checkUp(x,y, count, direction)
        checkRight(x,y, count, direction)
        checkDown(x,y, count, direction)
        randomCell(count,direction)
    else:
        randomCell(count,direction)
            
 

nextCell(startingX, startingY, count, 1)
#selectEndpoint()
drawMaze()