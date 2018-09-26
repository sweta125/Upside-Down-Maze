"""This file has 4 classes that create different types of mazes. Both
RandomHiddenMaze and RandomScrollMaze inherit from RandomMaze2D, and they
both CREATE random mazes in a hidden and scroll view, respectively.
Both ScrollMazeModified and HiddenMazeModified inherit from Maze2DModified,
and each object is responsible for transforming a given board and cellWalls
reference into their type of maze."""

from regularMaze import *

class RandomHiddenMaze(RandomMaze2D):
    name = "HIDDEN"
    
    def __init__(self, rows, cols, radius):
        super().__init__(rows, cols)
        self.radius = radius

    def getName(self):
        return RandomHiddenMaze.name
        
class RandomScrollMaze(RandomMaze2D):
    name = "SCROLL"
    
    def __init__(self, totalR, totalC, viewR, viewC):
        super().__init__(totalR, totalC)
        if viewR % 2 != 1: self.viewR = viewR+1
        elif viewR < 3: self.viewR = 3
        else: self.viewR = viewR
        
        if viewC % 2 != 1: self.viewC = viewC+1
        elif viewC < 3: self.viewC = 3
        else: self.viewC = viewC
    
    def getName(self):
        return RandomScrollMaze.name
    
    #this identical method needs to be accessed by ScrollMazeModified
    def getVisibleMaze(self, currentR, currentC):
        rows = len(self.getMaze())
        cols = len(self.getMaze()[0])
        visibleCells = 0
        side = 1
        d = {}
        lowestR, lowestC = False, False
        #if view level 1 -- need 9 so range is 2
        #if view level 3 -- need 49 (sides are 7) so range is  6
        #4,9,16,25, 36, 49, 64, 81...
        for i in range(self.viewR-1):
            for row in range(rows-1,-1,-1):
                if currentR-side <= row <= currentR+side:
                    for col in range(cols-1,-1,-1):
                        if currentC-side <= col <= currentC+side:
                            if lowestR == False and lowestC == False:
                                lowestR = row
                                lowestC = col
                            if row < lowestR: lowestR = row
                            if col < lowestC: lowestC = col
                            d[(row,col)] = self.getMaze()[row][col]
                            visibleCells += 1
            side += 1
        return (d, lowestR, lowestC)

class HiddenMazeModified(Maze2DModified):
    name = "HIDDEN"
    
    def __init__(self, board, cellWalls, radius):
        super().__init__(board, cellWalls)
        self.radius = radius
    
    def getName(self):
        return RandomHiddenMaze.name

class ScrollMazeModified(Maze2DModified):
    name = "SCROLL"
    
    def __init__(self, board, cellWalls, viewR, viewC):
        super().__init__(board, cellWalls)
        if viewR % 2 != 1: self.viewR = viewR+1
        elif viewR < 3: self.viewR = 3
        else: self.viewR = viewR
        
        if viewC % 2 != 1: self.viewC = viewC+1
        elif viewC < 3: self.viewC = 3
        else: self.viewC = viewC
    
    def getName(self):
        return RandomScrollMaze.name
    
    #this identical method needs to be accessed by RandomScrollMaze
    def getVisibleMaze(self, currentR, currentC):
        rows = len(self.getMaze())
        cols = len(self.getMaze()[0])
        visibleCells = 0
        side = 1
        d = {}
        lowestR, lowestC = False, False
        for i in range(self.viewR-1):
            for row in range(rows-1,-1,-1):
                if currentR-side <= row <= currentR+side:
                    for col in range(cols-1,-1,-1):
                        if currentC-side <= col <= currentC+side:
                            if lowestR == False and lowestC == False:
                                lowestR = row
                                lowestC = col
                            if row < lowestR: lowestR = row
                            if col < lowestC: lowestC = col
                            d[(row,col)] = self.getMaze()[row][col]
                            visibleCells += 1
            side += 1
        return (d, lowestR, lowestC)
