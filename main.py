# Example of script to build board fo "life of game"

# The grid is a 2D array of boolean
#  True = living cell
#  False = dead cell


import copy
import time
import random
import os


# Function to build a grid who take size in params
# @param height 
# @param width
# @return a grid (array of array of booleans) 
def buildGrid(height, width):
    grid = []
    
    for x in range(height):
        grid.append([])
        for y in range(width):
            grid[x].append(False)
    
    return grid

# Display the grid based on the 
def displayGrid(grid):
    gridToPrint = ""

    # for x in range(len(grid[0])):
    #     gridToPrint += " " + str(x)
    # gridToPrint += "\n"

    # y = 0

    for row in grid:
        # gridToPrint += str(y) + " "
        for cell in row:
            if cell:
                gridToPrint += "\033[1;47m  "
            else:
                gridToPrint += "\033[1;40m  "
        gridToPrint += "\n\33[0m"
        # y+=1

    print(gridToPrint)

# Fill randomly the grid based on "SPAWN_RATE"
def fillGridRandomly(grid):
    for x in range(height):
        for y in range(width):
            randomCell = random.randint(0, 10)
            if randomCell < SPAWN_RATE:
                grid[x][y] = True
    
# Count the living cells in an array of nearby cells
def countLiving(nearby):
    totalLiving = 0

    for cell in nearby:
        if cell:
            totalLiving += 1

    return totalLiving

# Return the next state of a cell, it depends on Game Of Live rules
def getNextStateByLivingNearby(totalLivingNearby, currentCellState):
    if totalLivingNearby == 2:
        return currentCellState

    if totalLivingNearby == 3:
        return True

    return False

# Run one simulation, for the given grid
def runOneSimulation(grid, height, width):
    # get a copy to return
    nextSilumation = copy.deepcopy(grid)

    # For each cell
    for x in range(height):
        for y in range(width):
            # put each cells around in a array
            nearby = []
            # first row
            if x > 0:
                if y > 0:
                    nearby.append(grid[x-1][y-1])
                nearby.append(grid[x-1][y])
                if y < width-1:
                    nearby.append(grid[x-1][y+1])
            
            # third row
            if y > 0:
                nearby.append(grid[x][y-1])
            # don't take the cell, only nearby
            if y < width-1:
                nearby.append(grid[x][y+1])
            
            # second row
            if x < height-1:
                if y > 0:
                    nearby.append(grid[x+1][y-1])
                nearby.append(grid[x+1][y])
                if y < width-1:
                    nearby.append(grid[x+1][y+1])
            
            # count how many living cell is around
            totalLivingNearby = countLiving(nearby)
            
            # Apply the ruls to the cell
            nextState = getNextStateByLivingNearby(totalLivingNearby, grid[x][y])


            # if totalLivingNearby != 0:
            #     print("------row------")
            #     print(x, y)
            #     print(nearby)
            #     print(totalLivingNearby, "from", grid[x][y], "to", nextState)
                

            nextSilumation[x][y] = nextState
        
        # displayGrid(grid)
    
    return nextSilumation


# -------- Start of the program --------

height=30
width=30
SPAWN_RATE=6
clear = lambda: os.system('clear')


# Build a grid with heaght and width
grid = buildGrid(height, width)
# Fill the grid with living cells
print("Silumation n°0")
fillGridRandomly(grid)
# Display First simulation
displayGrid(grid)


# With the grid builded, now run some simulation turn
silulationCount = 1
while True:
    clear()
    print("Silumation n°" + str(silulationCount))
    grid = runOneSimulation(grid, height, width)
    displayGrid(grid)
    silulationCount += 1
    time.sleep(0.2)

