"""This file encompasses two classes: RandomMaze2D and Maze2DModified.
RandomMaze2D generates a random maze given the number of rows and number
of columns wanted to create the maze. Maze2DModified "modifies" an existing maze:
given a 2D board and a cellWalls reference (that tells where the "walls" are
in a maze), the given board is made into a regular maze (i.e. functions same
as RandomMaze2D but they are generated differently)."""

import random

class RandomMaze2D(object):
    name = "REGULAR"

    def __init__(self, rows, cols, startRow=0, startCol=0, endRow=-1, endCol=-1):
        self.rows = rows
        self.cols = cols
       
        if not (0<=startRow<rows) or (0<=startCol<cols) or (0<=endRow<rows) \
        or (0<=endCol<cols): 
            self.startRow = 0
            self.startCol = 0
            self.endRow = self.rows-1
            self.endCol = self.cols-1
        else:
            self.startRow = startRow
            self.startCol = startCol
            self.endRow = endRow
            self.endCol = endCol
        
        self.board = [[0]*self.cols for i in range(self.rows)]
        self.cellWalls = createCellWallsDict(self)
        self.mazeIsCreated = False
    
    def __repr__(self):
        s = ""
        for row in range(self.rows):
            s += "\n"
            for col in range(self.cols):
                s += str(self.board[row][col]) + " "
        return s
    
    def getName(self):
        return RandomMaze2D.name
        
    def createPath(self):
        self.depth = 1
        self.board[self.startRow][self.startCol] = self.depth
        self.depth +=1
        self.board = createPathBuilder(self.board, self.startRow, \
            self.startCol, self.depth)
        self.cellWalls = RandomMaze2D.removeWall(self)
        self.mazeIsCreated = True
    
    def getMaze(self):
        return self.board
        
    def getCellWalls(self):
        return self.cellWalls
    #Can also reference Maze.cellWalls through instance name
    
    def removeWall(self):
        for row in range(self.rows):
            for col in range(self.cols):
                dirList = getPossibleDirections(row, col, self.rows, self.cols)
                for dir in dirList:
                    if dir == "UP":
                        if self.board[row][col] - 1 == self.board[row-1][col]:
                            self.cellWalls = removeWallHelper(self.cellWalls, \
                            row-1, col, row, col)
                    elif dir == "DOWN":
                        if self.board[row][col] - 1 == self.board[row+1][col]:
                            self.cellWalls = removeWallHelper(self.cellWalls, \
                            row+1, col, row, col)
                    elif dir == "LEFT":
                        if self.board[row][col] - 1 == self.board[row][col-1]:
                            self.cellWalls = removeWallHelper(self.cellWalls, \
                            row, col-1, row, col)
                    elif dir == "RIGHT":
                        if self.board[row][col] - 1 == self.board[row][col+1]:
                            self.cellWalls = removeWallHelper(self.cellWalls, \
                            row, col+1, row, col)
        return self.cellWalls
    
    #identical method accessed in Maze2DModified class
    def mazeSolver(self, currentRow, currentCol):
        tempBoard = [[0]*self.cols for i in range(self.rows)]
        if self.mazeIsCreated == True:
            temp = mazeSolverHelper(tempBoard, self.cellWalls, currentRow,\
            currentCol, self.endRow, self.endCol) #returns board
            return convertMazeListtoDict(temp)

class Maze2DModified(object):
    name = "REGULAR"
    
    def __init__(self, board, cellWalls):
        self.board = board
        self.cellWalls = cellWalls
        self.rows = len(self.board)
        self.cols = len(self.board[0])
        self.endRow = self.rows-1
        self.endCol = self.cols-1
    
    def getName(self):
        return RandomMaze2D.name
    
    def getMaze(self):
        return self.board
    
    def getCellWalls(self):
        return self.cellWalls
    
    """identical method accessed in RandomMaze2D class; 
    except for isMazeCreated boolean before"""
    def mazeSolver(self, currentRow, currentCol):
        tempBoard = [[0]*self.cols for i in range(self.rows)]
        temp = mazeSolverHelper(tempBoard, self.cellWalls, currentRow,\
            currentCol, self.endRow, self.endCol) #returns board
        return convertMazeListtoDict(temp)
        
#converts 2D board into a dict with nums as keys and (row, col) values
def convertMazeListtoDict(temp, count=None, d=None):
    if count == None or d == None:
        d = {}
        count = 1
    for row in range(len(temp)):
        for col in range(len(temp[0])):
            if temp[row][col] == count:
                d[count] = (row, col)
                return convertMazeListtoDict(temp, count+1, d)
    return d

def removeWallHelper(d, formerRow, formerCol, currentRow, currentCol):
    rowDiff = currentRow-formerRow
    colDiff = currentCol-formerCol
    if rowDiff > 0: #remove top wall
        #formerCol=currentCol can also say currentCol
        key = (formerRow, currentCol)
        try:d[key].remove("BOT")
        except ValueError: pass
    elif rowDiff < 0: #remove bottom wall
        key = (currentRow, currentCol)
        try: d[key].remove("BOT")
        except ValueError: pass
    elif colDiff < 0: #remove left wall
        key = (currentRow, currentCol)
        try: d[key].remove("RIGHT")
        except ValueError: pass
    elif colDiff > 0: #remove right wall
        key = (currentRow, formerCol)
        try: d[key].remove("RIGHT")
        except ValueError: pass
    else: pass
    return d

def createCellWallsDict(self):
    d = {}
    for row in range(self.rows):
        for col in range(self.cols):
            key = (row, col)
            """each cell defined by bottom and right hand wall to avoid
            overlap. For example, removing barrier between top
            and bottom otherwise."""
            d[key] = ["BOT", "RIGHT"]
    return d
        
"""board is filled with 0s; given a board (must be a non-ragged board but 
not necessarily square), returns maze path"""
def createPathBuilder(board, currentRow = None, currentCol = None, depth=None):
    rows, cols = len(board), len(board[0])
    if everyCellVisited(board, rows, cols):
        return board
    
    possibleDirs = getPossibleDirections(currentRow, currentCol, rows, cols)
    for i in range(len(possibleDirs)):
        nextMove = getRandomDirection(possibleDirs)
        possibleDirs.remove(nextMove)
        if nextMove != None:
            tempRow, tempCol = currentRow, currentCol
            if nextMove == 'UP': tempRow-=1
            elif nextMove == 'DOWN': tempRow+=1
            elif nextMove == 'LEFT':tempCol-=1
            #nextMove == 'RIGHT'
            else: tempCol+=1   

            if board[tempRow][tempCol] == 0:
                board[tempRow][tempCol] = depth
                depth+=1
                solution = createPathBuilder(board, tempRow, tempCol, depth)
                if solution != None:
                    return solution
                #makes drawing Walls easier if we don't reset
                #board[tempRow][tempCol] == 0
                depth-=1
    return None

def mazeSolverHelper(board, cellWalls, currentRow, currentCol, endRow, endCol, depth=None):
    rows, cols = len(board), len(board[0])
    if depth == None: 
        depth = 1
        board[currentRow][currentCol] = depth
        depth += 1
    if currentRow == endRow and currentCol == endCol:
        return board
    
    possibleDirs = getPossibleDirections(currentRow, currentCol, rows, cols)
    for i in range(len(possibleDirs)):
        nextMove = getRandomDirection(possibleDirs)
        possibleDirs.remove(nextMove)
        if isMovePossible(nextMove, cellWalls, currentRow, currentCol):
            tempRow, tempCol = currentRow, currentCol
            if nextMove == 'UP': tempRow-=1
            elif nextMove == 'DOWN': tempRow+=1
            elif nextMove == 'LEFT':tempCol-=1
            #nextMove == 'RIGHT'
            else: tempCol+=1   

            if board[tempRow][tempCol] == 0:
                board[tempRow][tempCol] = depth
                depth+=1
                solution = mazeSolverHelper(board, cellWalls, tempRow, tempCol,\
                 endRow, endCol, depth)
                if solution != None:
                    return solution
                #need to reset values here!
                board[tempRow][tempCol] = 0
                depth-=1
    return None

#aka is there a wall; d is dict for cellWalls
def isMovePossible(nextMove, d, currentRow, currentCol):
    if not (isinstance(nextMove, str)): return False
    if nextMove == 'UP': 
        key = (currentRow-1, currentCol)
        word = "BOT"
    elif nextMove == 'DOWN': 
        key = (currentRow, currentCol)
        word = "BOT"
    elif nextMove == 'LEFT':
        key = (currentRow, currentCol-1)
        word = "RIGHT"
    elif nextMove == 'RIGHT': 
        key = (currentRow, currentCol)
        word = "RIGHT"
    if key not in d:
        return False
    if word in d[key]:
        return False
    else:
        return True

def getPossibleDirections(currentRow, currentCol, totalRows, totalCols):
    if not (0<=currentRow<totalRows) and (0<=currentCol<totalCols):return None
    possDir = ['UP', 'DOWN', 'RIGHT', 'LEFT']
    if currentRow == 0:
        possDir.remove('UP')
    elif currentRow == totalRows-1:
        possDir.remove('DOWN')
    if currentCol == 0:
        possDir.remove('LEFT')
    elif currentCol == totalCols-1:
        possDir.remove('RIGHT')
    if len(possDir) == 0: return None
    else:
        return possDir

#takes in possDir (a list)
def getRandomDirection(possDir):
    rand = random.randint(0, len(possDir)-1)
    return possDir[rand]
            
def everyCellVisited(board, rows, cols):
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                return False
    return True