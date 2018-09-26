"""This file is the main file for playing the Game."""

from regularMaze import *
from differentMazes import *
from drawCharacters import *
from drawScreens import *
from actors import *
import random, math
from tkinter import *

"""The following template for events animation using tkinter was taken from 
the 15-112 course website (week 6); there is a comment near the bottom of 
the file with more details."""

def init(data):
    data.level = -1
    data.screenDisplay = "INTRO" #first screen displayed
    #used in animation of objects for intro screen
    data.s1, data.s2, data.s3, data.s4 = -10, -10, data.height, data.height
    data.levelText = False
    data.speed = 5
    data.timerCountdown = 1000
    data.time = 0
    data.areEnemies = False

def newGame(data, num=4):
    data.screenDisplay = "GAME"
    if not 1 <= num <= 7:
        num = 4
    #number of enemies automatically set
    if data.areEnemies == True: 
        if num == 1: numEnemies = 1
        else: numEnemies = num*2
    data.level = num
    data.rows = 5*data.level
    data.cols = 5*data.level
    data.board = [[0]*data.cols for i in range(data.rows)]
    
    """The game starts such that the initial maze is a scroll mazel
    the following are commented out but left in case creators wants to change:
    data.maze = RandomMaze2D(data.rows, data.cols)
    data.maze = RandomHiddenMaze(data.rows, data.cols, max(1,data.level//2+1))"""
    data.maze = RandomScrollMaze(data.rows, data.cols, 2*data.level+1, 2*data.level+1)
    data.cellSizeW, data.cellSizeH = data.width//data.cols, data.height//data.rows
    resize(data)
    data.maze.createPath()
    data.mazeVersions = False
    
    elevenInitialHealth, elevenStartR, elevenStartC = data.level*300, 0, 0
    data.hero = Survivor(elevenStartR, elevenStartC, "El", elevenInitialHealth)
    willInitialHealth, willR, willC = data.level*300, data.rows-1, data.cols-1
    data.victim = Survivor(willR, willC, "Will", willInitialHealth)
    
    data.enemyCollision = False
    data.mazeSolverCalculated = False
    data.hasWon = False
    data.direction = None
    if data.areEnemies == True: #from init(data)
        data.enemies = []
        initializeEnemies(data, numEnemies)

def initializeEnemies(data, numEnemies):
    count=1
    while (len(data.enemies) <= numEnemies-1):
        randRow = random.randint(0, data.rows-1)
        randCol = random.randint(0, data.cols-1)
        #certain distance between hero and each enemy at immediate start of game
        if (abs(data.hero.getUserR()-randRow) >= max(1,data.level//3) and \
        abs(data.hero.getUserC()-randCol) >= max(1,data.level//3)) \
        and (randRow != data.rows-1 and randCol != data.cols-1):
            randAttackPower = random.randint(30, 50)
            name = "Demagorgon%d" % count
            data.enemies.append(Enemy(randRow, randCol, name, randAttackPower))
        count+=1
    
def resize(data):
    if data.maze.name == "SCROLL":
        data.cellSizeW, data.cellSizeH = data.width//data.maze.viewC, \
        data.height//data.maze.viewR
    else: data.cellSizeW,data.cellSizeH=data.width//data.cols,data.height//data.rows
    
def mousePressed(event, data):
    if data.screenDisplay == "START":
        if data.width//8 <= event.x <= data.width//2-data.width//10 and \
        data.height//2+data.height//10 <= event.y <= data.height*2//3:
            data.areEnemies = True
        elif data.width*6//10 <= event.x <= data.width*9//10 and \
        data.height//2+data.height//10 <= event.y <= data.height*2//3:
            data.areEnemies = False

def keyPressed(event, data):
    data.mazeSolverCalculated = False
    if data.screenDisplay == "INTRO":
        if event.keysym == "space":
            data.screenDisplay = "START"
        else: data.screenDisplay = "INSTRUCTIONS"
    elif data.screenDisplay == "INSTRUCTIONS":
        if data.level > 0: data.screenDisplay = "GAME"
        else: data.screenDisplay = "START"
    elif data.screenDisplay == "START":
        if event.char.isdigit() and  1<= int(event.char) <= 7:
                data.level = int(event.char)
        
    elif data.screenDisplay == "GAME":
        if data.mazeVersions == True: #the game is paused to switch maze Versions
            if event.char == "1": #regular
                board = Maze2DModified(data.maze.getMaze(), data.maze.cellWalls)
                data.maze = board
                resize(data)
            elif event.char == "2": #hidden
                board = HiddenMazeModified(data.maze.getMaze(), \
                    data.maze.cellWalls, max(1,data.level//2+1))
                data.maze = board
                resize(data)
            elif event.char == "3": #scroll
                board = ScrollMazeModified(data.maze.getMaze(), \
                    data.maze.cellWalls, 2*data.level+1, 2*data.level+1)
                data.maze = board
                resize(data)
            data.mazeVersions = False
            
        if event.char == "e" or event.char == "E": 
            data.screenDisplay = "END"
        elif event.char == "i" or event.char == "I": 
            data.screenDisplay = "INSTRUCTIONS"
        
        elif event.keysym == "space":  #Scroll
            data.mazeVersions = True
        
        elif event.keysym == "Tab":
            getMazeSolver(data)
        
        elif event.keysym == "Up" or event.keysym == "Right" \
        or event.keysym == "Down" or event.keysym == "Left":
            movePerson(data, data.hero, str(event.keysym), 1)
                            
    elif data.screenDisplay == "END":
        if event.char == "s" or event.char == "S":
            init(data) #newGame called in timerFired
            data.screenDisplay = "START"
        elif event.keysym == "space":
            init(data)
            data.screenDisplay = "INTRO"
    
    else: pass
    
def timerFired(data):
    if data.screenDisplay == "INTRO": #animation of words!
        if data.s1 >= data.height//3: pass
        else: data.s1 += data.speed
        
        if data.s2 >= data.height//3+data.height//50: pass
        else: data.s2 += data.speed*3//2
        
        if data.s3 <= data.height//3+data.height//8: pass
        else: data.s3 -= data.speed*3//2
        
        if data.s4 <= data.height//3+data.height//50+data.height//8: pass
        else: data.s4 -= data.speed*2
        
    elif data.screenDisplay == "START":
        data.timerCountdown -= 10
        if data.timerCountdown <= 0:
            if data.level == -1: newGame(data, random.randint(1,7))
            else: newGame(data, data.level)
            data.screenDisplay = "GAME"
        elif data.level!=-1:
            data.levelText = True
    
    elif data.screenDisplay == "GAME":
        #checked when the game isn't paused at screen-switching option!
        if data.mazeVersions == False:
            #move Enemies each second
            if data.areEnemies == True and data.maze.name != "REGULAR":
                data.time += 10
                if(data.time == (data.time//100)*100):#second
                    for enem in data.enemies:
                        moveEnemyHelper(data, enem)
            #check for collisions every moment - not just when enemy moved
            if data.areEnemies == True:
                for enem in data.enemies:
                    checkCollisions(data, enem)
            
            """Eleven(hero)"s health diminishes during Regular mode and increases
            during Hidden mode; does not change durign Scroll mode"""
            if data.maze.name == "REGULAR":
                temp = data.hero.getUserHealth()
                data.hero.setUserHealth(temp-3)
            elif data.maze.name == "HIDDEN":
                temp = data.hero.getUserHealth()
                data.hero.setUserHealth(temp+2)
        
        #checks if Eleven reached Will! aka if game is won
        if data.hero.getUserR() == data.rows-1 and data.hero.getUserC() == data.cols-1:
            data.hasWon = True
            data.screenDisplay = "END"
        
        #checks if Game is lost - when either Eleven or Will have a health <= 0
        if data.victim.getUserHealth() <= 0 or data.hero.getUserHealth() <= 0:
            data.hasWon = False
            data.screenDisplay = "END"
        
        else: #Will's health is decreasing all the time no matter what Maze mode
            if data.mazeVersions == False:
                temp = data.victim.getUserHealth()
                data.victim.setUserHealth(temp-1)

def checkCollisions(data, mazePerson):
    if type(mazePerson) == Enemy: #check Collision when Enemy
        if mazePerson.getUserR() == data.hero.getUserR() and \
        mazePerson.getUserC() == data.hero.getUserC():
            impact = data.hero.getUserHealth() - mazePerson.getAttackPower()
            data.hero.setUserHealth(impact)
            data.enemyCollision = True
    elif type(mazePerson) == Survivor: #check Collisions when Survivor moves
        for enem in data.enemies:
            checkCollisions(data, enem)

def redrawAll(canvas, data):
    if data.screenDisplay == "INTRO":
        drawIntroScreen(data, canvas) 
        
    elif data.screenDisplay == "START":
        drawStartScreen(data, canvas)
    
    elif data.screenDisplay == "INSTRUCTIONS":
        drawInstructionScreen(data, canvas)
    
    elif data.screenDisplay == "GAME":
        if data.mazeVersions == False: 
            drawMazeBackground(data, canvas, "powder blue")
            if data.maze.name == "HIDDEN":
                drawMazeBackground(data, canvas, "DeepSkyBlue4")
                drawVisibleOpening(data, canvas)
        
        #drawn even when data.mazeVerions == True
        if data.maze.name != "HIDDEN":
            canvas.create_line(3, 0, 3, data.height, fill="midnight blue", width=3)
            canvas.create_line(0, 3, data.width, 3, fill="midnight blue", width=3)
        drawWallLines(data, canvas)
        
        if data.mazeSolverCalculated == True:
            drawMazeSolver(data, canvas)
            drawMazeHint(data, canvas)
        
        if data.mazeVersions == False:
            if data.maze.name == "SCROLL":
                drawCharWill(canvas, data.cellSizeW, data.cellSizeH, \
                data.rows-1-data.lowestR, data.cols-1-data.lowestC)
                if data.areEnemies == True and len(data.enemies) > 0:
                    for enem in data.enemies:
                        drawCharDemagorgon(canvas, data.cellSizeW, \
                        data.cellSizeH, enem.getUserR()-data.lowestR, \
                        enem.getUserC()-data.lowestC)
        
            else: #data.maze.name != "SCROLL"
                drawCharWill(canvas, data.cellSizeW, data.cellSizeH, \
                data.victim.getUserR(), data.victim.getUserC())
                if data.areEnemies == True and len(data.enemies) > 0:
                    for enem in data.enemies:
                        if data.maze.name == "HIDDEN":
                            if data.hero.getUserR()-data.maze.radius < enem.getUserR() \
                            <  data.hero.getUserR()+data.maze.radius and \
                            data.hero.getUserC()-data.maze.radius < enem.getUserC() < \
                            data.hero.getUserC()+data.maze.radius:
                                drawCharDemagorgon(canvas, data.cellSizeW, \
                                    data.cellSizeH, enem.getUserR(), enem.getUserC())
                        #REGULAR maze
                        else: 
                            drawCharDemagorgon(canvas, data.cellSizeW, \
                            data.cellSizeH, enem.getUserR(), enem.getUserC())
        
        if data.enemyCollision == True:
            if data.maze.name != "SCROLL": data.lowestR, data.lowestC = 0, 0
            canvas.create_rectangle((data.hero.getUserC()-data.lowestC)*data.cellSizeW,\
                (data.hero.getUserR()-data.lowestR)*data.cellSizeH, \
                (data.hero.getUserC()-data.lowestC)*data.cellSizeW+data.cellSizeW, \
                (data.hero.getUserR()-data.lowestR)*data.cellSizeH+data.cellSizeH, \
                fill="yellow")
            data.enemyCollision = False
            
        if data.mazeVersions == False:
            drawShorthandInstructions(data, canvas)
        
        drawMovingUser(data, canvas)
        
        if data.mazeVersions == True:
            drawMazeOptions(data, canvas)
            drawHealthBars(data, canvas)
        
    elif data.screenDisplay == "END":
        drawGameOverScreen(data, canvas)
        
    else: pass

def moveEnemyHelper(data, enemy):
    moved = False
    while (moved == False):
        listMoves = ["Up", "Down", "Left", "Right"]
        rand = random.randint(0,len(listMoves)-1)
        try:
            move = listMoves.pop(rand)
            if movePerson(data, enemy, move, 1) == True:
                moved = True
        except: pass
    
#direction is formated to a string: "Up", "Down", "Left", and "Right"
#mazePerson is an instance and NOT a class reference
def movePerson(data, mazePerson, dir=None, steps=1):
    temp = False
    if mazePerson == data.hero: #data.direction used later!
        data.direction = dir
    reference = data.maze.cellWalls
    if dir == "Up":
        key = (mazePerson.getUserR()-1, mazePerson.getUserC())
        if key in reference and "BOT" in reference[key]: pass
        else: 
            temp = mazePerson.getUserR()-steps
            mazePerson.setUserR(temp)
            temp = True
        
    elif dir == "Down":
        key = (mazePerson.getUserR(), mazePerson.getUserC())
        if key in reference and "BOT" in reference[key]: pass
        else: 
            temp = mazePerson.getUserR()+steps
            mazePerson.setUserR(temp)
            temp = True
        
    elif dir == "Left":
        key = (mazePerson.getUserR(), mazePerson.getUserC()-1)
        if key in reference and "RIGHT" in reference[key]: pass
        else: 
            temp = mazePerson.getUserC()-steps
            mazePerson.setUserC(temp)
            temp = True
        
    elif dir == "Right":
        key = (mazePerson.getUserR(), mazePerson.getUserC())
        if key in reference and "RIGHT" in reference[key]: pass
        else: 
            temp = mazePerson.getUserC()+steps
            mazePerson.setUserC(temp)
            temp = True
    
    if type(mazePerson) == Survivor and data.areEnemies == True: 
        checkCollisions(data, data.hero)
    wrapPersonPosition(data, mazePerson, mazePerson.getUserR(), mazePerson.getUserC())
    return temp

def wrapPersonPosition(data, mazePerson, currentRow, currentCol):
    if currentRow < 0:
        mazePerson.setUserR(0)
    elif currentRow > data.rows-1:
        mazePerson.setUserR(data.rows-1)
            
    if currentCol < 0:
        mazePerson.setUserC(0)
    elif currentCol > data.cols-1:
        mazePerson.setUserC(data.cols-1)
    
    if type(mazePerson) == Enemy:
        if currentRow == data.rows-1 and currentCol == data.cols-1:
            data.enemies.remove(mazePerson) #so it's not on will

def getMazeSolver(data):
    data.solve = data.maze.mazeSolver(data.hero.getUserR(), data.hero.getUserC())
    data.mazeSolverCalculated = True

def drawVisibleOpening(data, canvas):
    x1, y1, x2, y2 = data.hero.getUserC()-data.maze.radius, \
    data.hero.getUserR()-data.maze.radius, data.hero.getUserC()+data.maze.radius,\
     data.hero.getUserR()+data.maze.radius
    if x1 < 0: 
        x1 = -1
    elif y1 < 0: 
        y1 = -1
    elif x2 > data.cols-1: 
        x2 = data.cols
    elif y2 > data.rows-1: 
        y2 = data.rows
    
    canvas.create_oval(x1*data.cellSizeW+data.cellSizeW//4, \
        y1*data.cellSizeH+data.cellSizeH//4,x2*data.cellSizeW+3*data.cellSizeW//4, 
        y2*data.cellSizeH+3*data.cellSizeH//4, fill="white", \
        outline="sea green", width = 2)

def drawHealthBars(data, canvas):
    calcWillHealth = str(int((data.victim.getUserHealth())/data.victim.getInitialHealth()*100))
    calcElevenHealth = str(int((data.hero.getUserHealth())/data.hero.getInitialHealth()*100))
    canvas.create_rectangle(data.width//8, data.height*2//3, data.width*9//20, \
        data.height*3//4, fill="light coral", width=3)
    canvas.create_rectangle(data.width*13//24, data.height*2//3, data.width*18//20,\
        data.height*3//4, fill="light coral", width = 3)
    canvas.create_text(data.width*9//32, data.height*17//24, \
        text="Will's Health: "+calcWillHealth+"%", font="Cambria 15")
    canvas.create_text(data.width*23//32, data.height*17//24, \
        text="Eleven's Health: "+calcElevenHealth+"%", font="Cambria 15")

def drawShorthandInstructions(data, canvas):
    s=("Press 'Spacebar' to switch maze view\nPress 'i' for instructions"
    "\nPress 'Tab' for maze hint\nPress 'e' to exit")
    if data.maze.name == "SCROLL" or data.maze.name == "REGULAR":
        canvas.create_text(data.width//27, data.height*35//40, text=s, \
        anchor=NW, fill="deep pink", font="Cambria 10")
    elif data.maze.name == "HIDDEN":
        if data.hero.getUserR() > data.rows//2 and \
        data.hero.getUserC() < data.cols*3//4:
            x , y = (data.height*8//10, data.height//10)
            anchor = NE
        else: 
            x , y = data.width//27, data.height*3//4
            anchor = NW
        canvas.create_text(x, y, text=s, anchor=anchor, fill="salmon", font="Cambria 20")

def drawMovingUser(data, canvas):
    if data.maze.name == "REGULAR" or data.maze.name == "HIDDEN":
        data.drawUserR, data.drawUserC = data.hero.getUserR(), data.hero.getUserC()
    elif data.maze.name == "SCROLL":
        data.drawUserR = data.hero.getUserR()-data.lowestR
        data.drawUserC =  data.hero.getUserC()-data.lowestC
        
    cSW, cSH = data.cellSizeW, data.cellSizeH
    uR, uC = data.drawUserR, data.drawUserC
    
    if data.direction == "Right": drawCharElevenRight(canvas, cSW, cSH, uR, uC)
    elif data.direction == "Left": drawCharElevenLeft(canvas, cSW, cSH, uR, uC)
    elif data.direction == "Up": drawCharElevenBack(canvas, cSW, cSH, uR, uC)
    else: drawCharElevenFront(canvas, cSW, cSH, uR, uC)
    #Else works on the "None" case when init called

def drawMazeBackground(data, canvas, backColor):
    canvas.create_rectangle(0,0,data.width,data.height,fill=backColor)
    a = [(random.randint(0,8)) for i in range(max(5, (data.width+data.height)//50))]
    b = ["dodger blue", "RosyBrown2", "lime green", "yellow", "maroon2", \
        "white", "white smoke", "lemon chiffon"]
    for item in a:
        x1 = data.cellSizeW*(random.randint(0,data.rows-1))
        y1 = data.cellSizeH*(random.randint(0, data.rows-1))
        colorIndex = random.randint(0, len(b)-1)
        canvas.create_oval(x1, y1, x1+item, y1+item, fill = b[colorIndex], width=0)
    
def drawWallLines(data, canvas):
    #for regular Maze2D type
    rowLowerB, rowUpperB, colLowerB, colUpperB = 0, data.rows-1, 0, data.cols-1 
    if data.maze.name == "REGULAR": pass
    elif data.maze.name == "HIDDEN":
        rowLowerB = max(0,data.hero.getUserR()-data.maze.radius)
        rowUpperB = min(data.rows-1,data.hero.getUserR()+data.maze.radius)
        colLowerB = max(0,data.hero.getUserC()-data.maze.radius)
        colUpperB = min(data.cols-1,data.hero.getUserC()+data.maze.radius)
    elif data.maze.name == "SCROLL":
        #referenced these as data because use them in drawMovingUser function
        reference, data.lowestR, data.lowestC = \
        data.maze.getVisibleMaze(data.hero.getUserR()+data.maze.viewR//2, \
        data.hero.getUserC()+data.maze.viewC//2)
    
    for key in data.maze.cellWalls:
        row, col = key
        color="midnight blue"
        if data.maze.name == "HIDDEN":
            if rowLowerB <= row <= rowUpperB and colLowerB <= col <= colUpperB:
                drawR, drawC = row, col
                color="DeepSkyBlue4"
            else: continue
        elif data.maze.name == "SCROLL":
            drawR, drawC = row-data.lowestR, col-data.lowestC
        elif data.maze.name == "REGULAR":
            drawR, drawC = row, col
       
        wallList = data.maze.cellWalls[key] 
        if "BOT" in wallList:
            canvas.create_line(drawC*data.cellSizeW, 
            drawR*data.cellSizeH+data.cellSizeH, 
            drawC*data.cellSizeW+data.cellSizeW, drawR*data.cellSizeH+data.cellSizeH, 
            fill=color, width=3)
        if "RIGHT" in wallList:
            canvas.create_line(drawC*data.cellSizeW+data.cellSizeW, 
            drawR*data.cellSizeH, drawC*data.cellSizeW+data.cellSizeW, 
            drawR*data.cellSizeH+data.cellSizeH, fill=color, width=3)

def drawMazeHint(data, canvas):
    if data.mazeSolverCalculated == True: 
        if data.maze.name == "REGULAR":
            if (len(data.solve)) >= 13: row, col = data.solve[13]
            elif (len(data.solve)) >= 6: row, col = data.solve[6]
            elif (len(data.solve)) >= 3: row, col = data.solve[3]
            else: row, col = data.solve[2]
        elif data.maze.name == "HIDDEN":
            try: row, col = data.solve[data.maze.radius+1]
            except: row, col = data.solve[2]
        elif data.maze.name == "SCROLL":
            return
        drawWaffle(canvas, data.cellSizeW, data.cellSizeH, row, col)
        
def drawMazeSolver(data, canvas):
    if data.mazeSolverCalculated == True:
        if data.maze.name == "HIDDEN": return
        max = len(data.solve)
        for index in range(1, max):
            row1, col1 = data.solve[index]
            row2, col2 = data.solve[index+1]
            if data.maze.name == "SCROLL":
                row1 -= data.lowestR
                row2 -= data.lowestR
                col1 -= data.lowestC
                col2 -= data.lowestC
            canvas.create_line(col1*data.cellSizeW+data.cellSizeW//2, 
                row1*data.cellSizeH+data.cellSizeH//2, 
                col2*data.cellSizeW+data.cellSizeW//2, 
                row2*data.cellSizeH+data.cellSizeH//2, fill="SlateBlue1", 
                dash=(5, 1, 2, 1), dashoff=3, width=3)

"""The following code was taken from the 15-112 course website. Week 6
gives an events animation template. I used this template so that I could
animate events on a canvas (my only tkinter widget). Data is kinda a struct
used to access "global" variables. Note that this game runs in a 600X600
screen upon running the file, but this can be changed."""
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.title("MazeEl")
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(600, 600)