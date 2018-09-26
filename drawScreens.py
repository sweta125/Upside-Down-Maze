"""This file has the functions for drawing various screens shown in the
main Game. All functions take in data and canvas as arguments, and draw
using tkinter. Most screens need to draw characters too (so this file imports
from characters)."""
import random
from tkinter import *
from drawCharacters import *

def drawMazeOptions(data, canvas):
    canvas.create_rectangle(data.width//3, data.height//6-data.height//7, \
        data.width*2//3, data.height//6-data.height//7+data.height//10, \
        fill="magenta3", activefill="MediumPurple1")
    canvas.create_rectangle(data.width//3, data.height*5//12-data.height//5, \
        data.width*2//3, data.height*5//12-data.height//5+data.height//10, \
        fill="magenta3", activefill="MediumPurple1")
    canvas.create_rectangle(data.width//3, data.height*2//3-data.height//5, \
        data.width*2//3, data.height*2//3-data.height//5+data.height//10, \
        fill="magenta3", activefill="MediumPurple1")
    canvas.create_text(data.width//2, data.height//6-data.height//12, \
        anchor=S, fill="white", text="1. Regular Maze View", font="Cambria 15")
    canvas.create_text(data.width//2, data.height*5//12-data.height//8, \
        anchor=S, fill="white", text="2. Hidden Maze View", font="Cambria 15")
    canvas.create_text(data.width//2, data.height*2//3-data.height//8, \
        anchor=S, fill="white", text="3. Scroll Maze View", font="Cambria 15")
    canvas.create_text(data.width//2, data.height*3//4+data.height//8, \
        fill="MediumPurple1", font= "Cambria 20 italic", \
        text="Press 1, 2, or 3 for options\nor any other key to resume")
        
def drawGameOverScreen(data, canvas):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="PaleVioletRed1")
    a = [(random.randint(0,8)) for i in range(max(5, (data.width+data.height)//50))]
    b = ["light sea green", "cadet blue", "dark violet", "SeaGreen2", "cornflower blue", "white"]
    for item in a:
        x1 = random.randint(1, data.width-1)
        y1 = random.randint(1, data.height-1)
        colorIndex = random.randint(0, len(b)-1)
        canvas.create_oval(x1, y1, x1+item, y1+item, fill = b[colorIndex], width=0)
    if data.hasWon == True:
        s = "Game Over: \nYou saved Will!"
    else: #data.hasWon == False
        s = "Game Over:\nMaybe next time you\n can beat The Upside Down"
    canvas.create_text(data.width//2, data.height//4, 
        text = s, font="Cambria 30 bold", fill="black")
    canvas.create_text(data.width*2//3, data.height//2+data.height//20, \
        text = "Press 's' to replay", font="Cambria 30 italic", fill="DarkOrchid4", \
        anchor=CENTER)
    canvas.create_text(data.width*2//3, data.height*2//3+data.height//20, \
        text = "Press 'Spacebar' to restart\nfrom the beginning", \
        font="Cambria 20 italic", fill="DarkOrchid4", anchor=CENTER)
    drawCharElevenFront(canvas, 100, 100, 5, 0)
    drawCharWill(canvas, 100, 100, 5, 1)
    

def drawStartScreen(data, canvas):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="red4")
    s = ("Type in a number from 1-7 (inclusive)\n to choose your maze level\nand" 
         " start the game: \n~less intense (1) to more intense (7)~")
    canvas.create_text(data.width//2, data.height//7, fill="plum3", font="Cambria 20", \
        text=s, anchor=CENTER)
    canvas.create_text(data.width//2, data.height*3//4, fill="sienna", font="Cambria 20", \
        text="Else random level with NO enemies will begin;\n\t Game starts in %d" \
        % (data.timerCountdown//100), anchor=CENTER)
    if data.levelText == True:
        canvas.create_text(data.width//2, data.height//3, fill="white", \
        font="Cambria 30", text="Level: %d" % (data.level), anchor=CENTER)
    canvas.create_text(data.width//2, data.height//2, fill="plum3", \
        font="Cambria 20", \
        text="Click the box 'Yes' or 'No'\nif you want optional enemies:", \
        anchor=CENTER)
    yesW = 0
    noW = 3 #default is there are no enemies
    if data.areEnemies == True: 
        yesW = 3
        noW = 0
    canvas.create_rectangle(data.width//8, data.height//2+data.height//10, \
        data.width//2-data.width//10, data.height*2//3, fill="cornflower blue", \
        activefill="white", width=yesW)
    canvas.create_rectangle(data.width*6//10, data.height//2+data.height//10, \
        data.width*9//10, data.height*2//3, fill="cornflower blue", \
        activefill="white", width=noW)
    canvas.create_text(data.width//4, data.height*2//3-data.height//25, \
        text="YES", font="Cambria 18")
    canvas.create_text(data.width*3//4, data.height*2//3-data.height//25, \
        text="NO", font="Cambria 18")
    canvas.create_line(10,10,data.width-10,10,fill="cyan", dash=(5,3,1), width = 3)
    canvas.create_line(10,10,10,data.height-10,fill="cyan", dash=(5,3,1), width = 3)
    canvas.create_line(10,data.height-10,data.width-10,data.height-10,\
        fill="cyan", dash=(5,3,1), width = 3)
    canvas.create_line(data.width-10,data.height-10,data.width-10,10, \
        fill="cyan", dash=(5,3,1), width = 3)
    for i in range(10):
        drawWaffle(canvas, data.width//10, data.height//10, 8.5, i)
    
def drawInstructionScreen(data, canvas):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="light steel blue")
    canvas.create_text(data.width//2, data.height//15, fill="SpringGreen3", \
        font="Cambria 30 bold", text="INSTRUCTIONS")
    s1="In the realm of..."
    canvas.create_text(data.width//5, data.height//7, text=s1, \
        font="Cambria 16", fill="red4")
    s2="STRANGER THINGS"
    canvas.create_text(data.width*12//20, data.height*7//40, text=s2, \
        font="Courier 25 italic bold", fill="red4")
    s3="...Eleven (El) has to save Will!"
    canvas.create_text(data.width*7//10, data.height//4, text=s3, \
        font="Cambria 16", fill="red4")
    drawCharElevenFront(canvas, 100, 100, 1, 0)
    drawCharWill(canvas, 100, 100, 1, 1)
    drawCharDemagorgon(canvas, 100, 100, 1.75, 4.5)
    s4=("It looks like The Upside Down is testing\n your maze solving skills;"
        " to save Will, \nyou need to solve the maze by reaching his character.")
    canvas.create_text(data.width*9//20, data.height*4//10, text=s4, \
        font="Cambria 16", fill="dark green", anchor=CENTER)
    s5="Use the Up, Down, Right, and Left arrow keys to move\nthroughout the maze. Avoid demagorgons!"
    canvas.create_text(data.width*9//20, data.height*21//40-data.height//50, \
        text=s5, font="Cambria 16", fill="blue4", anchor=CENTER)
    s6="There are 3 different views of the maze: Regular,\nHidden, and Scroll."+ \
        " You will start out in the Scroll view.\n(Hint: Different mazes may affect El's health!)"
    canvas.create_text(data.width*9//20, data.height*25//40-data.height//40, \
        text=s6, font="Cambria 16", fill="blue4", anchor=CENTER)
    s7="To switch the maze view AND see\ncharacters' health, press " + \
        "'Spacebar'\nthen type 1, 2, or 3 accordingly"
    canvas.create_text(data.width*6//20, data.height*29//40, text=s7, \
        font="Cambria 12", fill="IndianRed3", anchor=CENTER)
    s8="To return to this instruction\nscreen (pausing the game),\n press 'i'"
    canvas.create_text(data.width*6//20, data.height*34//40, text=s8, \
        font="Cambria 12", fill="IndianRed3", anchor=CENTER)
    s9="To get hints about solving the\n maze, press 'Tab' (El's favorite!)"
    canvas.create_text(data.width*15//20, data.height*28//40, \
        text=s9, font="Cambria 12", fill="IndianRed3", anchor=CENTER)
    drawWaffle(canvas,100,100,4.3,4)
    s10="To forfeit the game, press 'e'"
    canvas.create_text(data.width*15//20, data.height*35//40, text=s10, \
        font="Cambria 12", fill="IndianRed3", anchor=CENTER)
    s11="Got it? Will needs your help! Press any key to continue!"
    canvas.create_text(data.width//2, data.height*38//40, text=s11, \
        font="Cambria 18", fill="red", anchor=CENTER)

def drawIntroScreen(data, canvas):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="black")
    a = [(random.randint(0,5)) for i in range(20)]
    b = ["OrangeRed2", "OrangeRed3", "OrangeRed4", "red2", "maroon", \
        "firebrick3", "DarkOrange3", "DarkOrange4"]
    for item in a:
        x1 = (random.randint(1,data.width-1))
        y1 = (random.randint(1,data.height-1))
        x2 = (random.randint(1,data.width-1))
        y2 = (random.randint(1,data.height-1))
        colorIndex = random.randint(0, len(b)-1)
        canvas.create_line(x1, y1, x2, y2, fill = b[colorIndex], width=item)
    canvas.create_text(data.width//2, data.s1, 
        text = "The Upside Down:", font="Courier 30 bold", fill="red4", anchor=CENTER)
    canvas.create_text(data.width//2, data.s2, 
        text = "The Upside Down:", font="Courier 30 bold", fill="salmon", \
        activefill="plum3", anchor=CENTER)
    canvas.create_text(data.width//2, data.s3, 
        text = "Maze 11", font="Courier 30 bold", fill="red4", anchor=CENTER)
    canvas.create_text(data.width//2, data.s4, 
        text = "Maze 11", font="Courier 30 bold", fill="salmon", \
        activefill="plum3", anchor=CENTER)
    canvas.create_text(data.width//5, data.width*4//5, fill="gold2", \
        text="Press a key\n to see instructions", font="Arial 12 italic bold", \
        activefill="yellow")
    canvas.create_text(data.width*4//5, data.width*4//5, fill="gold2", \
        text="Press SPACEBAR\n to start the game", font="Arial 12 italic bold", \
        activefill="yellow")