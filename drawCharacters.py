"""This file draws all the images (Eleven, Will, Demagorgon, and a Waffle) used
in the game. All functions take in canvas, cellSizeWidth(cSW), cellSizeH (cSH),
row to draw image (uR) and col to draw image (C). They also take optional
speed parameters to move the images. Images are drawn through tkinter."""

from tkinter import *

def drawWaffle(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//4+(cSW*uC+xSpeed), cSH//4+(cSH*uR+ySpeed), \
        cSW*3//4+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed), fill="goldenrod", \
        width=2, outline="dark goldenrod")
    canvas.create_line(cSW//3+(cSW*uC+xSpeed), cSH*5//16+(cSH*uR+ySpeed), \
        cSW//3+(cSW*uC+xSpeed), cSH*11//16+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*5//12+(cSW*uC+xSpeed), cSH*17//64+(cSH*uR+ySpeed), \
        cSW*5//12+(cSW*uC+xSpeed), cSH*47//64+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW//2+(cSW*uC+xSpeed), cSH//4+(cSH*uR+ySpeed), \
        cSW//2+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*7//12+(cSW*uC+xSpeed), cSH*17//64+(cSH*uR+ySpeed), \
        cSW*7//12+(cSW*uC+xSpeed), cSH*47//64+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*2//3+(cSW*uC+xSpeed), cSH*5//16+(cSH*uR+ySpeed), \
        cSW*2//3+(cSW*uC+xSpeed), cSH*11//16+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*5//16+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), \
        cSW*11//16+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*17//64+(cSW*uC+xSpeed), cSH*5//12+(cSH*uR+ySpeed), \
     cSW*47//64+(cSW*uC+xSpeed), cSH*5//12+(cSH*uR+ySpeed), width=2, \
     fill="dark goldenrod")
    canvas.create_line(cSW//4+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), \
        cSW*3//4+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*17//64+(cSW*uC+xSpeed), cSH*7//12+(cSH*uR+ySpeed), \
        cSW*47//64+(cSW*uC+xSpeed), cSH*7//12+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    canvas.create_line(cSW*5//16+(cSW*uC+xSpeed), cSH*2//3+(cSH*uR+ySpeed), \
        cSW*11//16+(cSW*uC+xSpeed), cSH*2//3+(cSH*uR+ySpeed), width=2, \
        fill="dark goldenrod")
    
def drawCharDemagorgon(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW*14/32+(cSW*uC), cSH//4+(cSH*uR), cSW*18//32+(cSW*uC), \
        cSH//8+(cSH*uR), fill="dark green", width=5, outline="green4")
    canvas.create_oval(cSW*7/32+(cSW*uC), cSH*6//24+(cSH*uR), \
        cSW*12//32+(cSW*uC), cSH*19//48+(cSH*uR), fill="dark green", width=5, \
        outline="green4")
    canvas.create_oval(cSW*20/32+(cSW*uC), cSH*6//24+(cSH*uR), cSW*25//32+(cSW*uC), \
        cSH*19//48+(cSH*uR), fill="dark green", width=5, outline="green4")
    canvas.create_oval(cSW*17//32+(cSW*uC), cSH*11//24+(cSH*uR), cSW*23//32+(cSW*uC), \
        cSH*31//48+(cSH*uR), fill="dark green", width=5, outline="green4")
    canvas.create_oval(cSW*9//32+(cSW*uC), cSH*11//24+(cSH*uR), cSW*15//32+(cSW*uC), \
        cSH*31//48+(cSH*uR), fill="dark green", width=5, outline="green4")
    canvas.create_line(cSW*4//8+(cSW*uC), cSH//4+(cSH*uR), cSW//2+(cSW*uC), \
        cSH//6+(cSH*uR), fill="red3", width=3)
    canvas.create_line(cSW*3//8+(cSW*uC), cSH//3+(cSH*uR), cSW//4+(cSW*uC), \
        cSH*15//48+(cSH*uR), fill="red3", width=3)
    canvas.create_line(cSW*5//8+(cSW*uC), cSH//3+(cSH*uR), cSW*6//8+(cSW*uC), \
        cSH*15//48+(cSH*uR), fill="red3", width=3)
    canvas.create_line(cSW*7//16+(cSW*uC), cSH*23//48+(cSH*uR), cSW*5//16+(cSW*uC), \
        cSH*30//48+(cSH*uR), fill="red3", width=3)
    canvas.create_line(cSW*9//16+(cSW*uC), cSH*23//48+(cSH*uR), cSW*11//16+(cSW*uC), \
        cSH*30//48+(cSH*uR), fill="red3", width=3)
    canvas.create_oval(cSW*3//8+(cSW*uC), cSH*2//8+(cSH*uR), cSW*5//8+(cSW*uC), \
        cSH//2+(cSH*uR), outline="slate gray", width=4, fill="red3")
    canvas.create_oval(cSW*7//16+(cSW*uC), cSH*5//16+(cSH*uR), cSW*9//16+(cSW*uC), \
        cSH*7//16+(cSH*uR), width=4, fill="red4", outline="slate gray")

def drawCharWill(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//3+(uC*cSW+xSpeed), cSH//8+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed), fill="burlywood1", width=0)
    canvas.create_oval(cSW*4//10+(uC*cSW+xSpeed), cSH//5+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH//4+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*11//20+(uC*cSW+xSpeed), cSH//5+(uR*cSH+ySpeed),\
        cSW*12//20+(uC*cSW+xSpeed), cSH//4+(uR*cSH+ySpeed), fill="black")  
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=0, \
        fill="saddle brown", style=PIESLICE, outline="saddle brown")
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=90, \
        fill="saddle brown", style=PIESLICE, outline="saddle brown")
    points = ((cSW//2+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed)), \
        (cSW//3+(uC*cSW+xSpeed), cSH*2//3+(uR*cSH+ySpeed)), (cSW*2//3+(uC*cSW+xSpeed), \
        cSH*2//3+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="firebrick4")
    canvas.create_rectangle(cSW*9//24+(uC*cSW+xSpeed), cSH*2//3+(uR*cSH+ySpeed), \
        cSW*11/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="dark khaki", width=0)
    canvas.create_rectangle(cSW*13//24+(uC*cSW+xSpeed), cSH*2//3+(uR*cSH+ySpeed), \
        cSW*15/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="dark khaki", width=0)
    canvas.create_oval(cSW*9//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed), \
        cSW*11/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*13//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed), \
        cSW*15/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*9//20+(uC*cSW+xSpeed), cSH*7//24+(uR*cSH+ySpeed), \
        cSW*11//20+(uC*cSW+xSpeed), cSH*9//24+(uR*cSH+ySpeed), fill="red3", outline="red3")
    points = ((cSW*9//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*8//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*7//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*8//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="firebrick4")
    canvas.create_rectangle(cSW*8//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), \
        fill="firebrick4", width=0)
    canvas.create_rectangle(cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), fill="firebrick4", \
        width=0)
    points = ((cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*13//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*12//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="firebrick4")

def drawCharElevenFront(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//3+(uC*cSW+xSpeed), cSH//8+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed), fill="burlywood1", \
        width=0)
    canvas.create_rectangle(cSW*7//24+(uC*cSW+xSpeed),cSH//8+(uR*cSH+ySpeed), \
        cSW*9//24+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), fill="gold2", width=0)
    canvas.create_rectangle(cSW*15//24+(uC*cSW+xSpeed),cSH//8+(uR*cSH+ySpeed), \
        cSW*17//24+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), fill="gold2", width=0)
    canvas.create_oval(cSW*4//10+(uC*cSW+xSpeed), cSH//5+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH//4+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*11//20+(uC*cSW+xSpeed), cSH//5+(uR*cSH+ySpeed), 
        cSW*12//20+(uC*cSW+xSpeed), cSH//4+(uR*cSH+ySpeed), fill="black")  
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), 
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=0, 
        fill="gold2", style=PIESLICE, outline="gold2")
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), 
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=90, 
        fill="gold2", style=PIESLICE, outline="gold2")
    points = ((cSW//2+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed)), 
        (cSW//3+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed)), 
        (cSW*2//3+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="light coral")
    canvas.create_rectangle(cSW*9//24+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed),\
        cSW*11/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="LightCyan2", width=0)
    canvas.create_rectangle(cSW*13//24+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed),\
        cSW*15/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="LightCyan2", width=0)
    canvas.create_oval(cSW*9//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed),\
        cSW*11/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*13//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed),\
        cSW*15/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    canvas.create_arc(cSW*9//20+(uC*cSW+xSpeed), cSH*7//24+(uR*cSH+ySpeed), \
        cSW*11//20+(uC*cSW+xSpeed), cSH*9//24+(uR*cSH+ySpeed), fill="red3", \
        start=180, outline="red3")
    canvas.create_arc(cSW*11//20+(uC*cSW+xSpeed), cSH*7//24+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH*9//24+(uR*cSH+ySpeed), fill="red3", \
        start=270, outline="red3")
    points = ((cSW*9//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*8//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*7//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*8//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="navy")
    canvas.create_rectangle(cSW*8//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), fill="navy", width=0)
    canvas.create_rectangle(cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), fill="navy", width=0)
    points = ((cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*13//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*12//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="navy")

def drawCharElevenBack(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//3+(uC*cSW+xSpeed), cSH//8+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed), fill="burlywood1", width=0)
    canvas.create_rectangle(cSW*7//24+(uC*cSW+xSpeed),cSH//8+(uR*cSH+ySpeed), \
        cSW*9//24+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), fill="gold2", width=0)
    canvas.create_rectangle(cSW*15//24+(uC*cSW+xSpeed),cSH//8+(uR*cSH+ySpeed), \
        cSW*17//24+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), fill="gold2", width=0)
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=0, fill="gold2", 
        style=PIESLICE, outline="gold2")
    canvas.create_arc(cSW//3+(uC*cSW+xSpeed), cSH//10+(uR*cSH+ySpeed), \
        cSW*4//6+(uC*cSW+xSpeed), cSH*3//10+(uR*cSH+ySpeed), start=90, fill="gold2", 
        style=PIESLICE, outline="gold2")
    points = ((cSW//2+(uC*cSW+xSpeed), cSH*2//5+(uR*cSH+ySpeed)), \
        (cSW//3+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed)), (cSW*2//3+(uC*cSW+xSpeed), \
        cSH*3//4+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="light coral")
    canvas.create_rectangle(cSW*9//24+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed), \
        cSW*11/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="LightCyan2", width=0)
    canvas.create_rectangle(cSW*13//24+(uC*cSW+xSpeed), cSH*3//4+(uR*cSH+ySpeed), 
        cSW*15/24+(uC*cSW+xSpeed), cSH*7//8+(uR*cSH+ySpeed), fill="LightCyan2", width=0)
    canvas.create_oval(cSW*9//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed), \
        cSW*11/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    canvas.create_oval(cSW*13//24+(uC*cSW+xSpeed), cSH*13//16+(uR*cSH+ySpeed), \
        cSW*15/24+(uC*cSW+xSpeed), cSH*14//16+(uR*cSH+ySpeed), fill="black")
    points = ((cSW*9//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*8//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), \
        (cSW*7//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)),(cSW*8//20+(uC*cSW+xSpeed),\
         cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="navy")
    canvas.create_rectangle(cSW*8//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*9//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), fill="navy", width=0)
    canvas.create_rectangle(cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed), \
        cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed), fill="navy", width=0)
    points = ((cSW*11//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)), \
        (cSW*12//20+(uC*cSW+xSpeed), cSH*6//10+(uR*cSH+ySpeed)), (cSW*13//20+(uC*cSW+xSpeed),\
        cSH*6//10+(uR*cSH+ySpeed)),(cSW*12//20+(uC*cSW+xSpeed), cSH//2+(uR*cSH+ySpeed)))
    canvas.create_polygon(points, fill="navy")

def drawCharElevenRight(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//3+(cSW*uC+xSpeed), cSH//8+(cSH*uR+ySpeed), \
        cSW*4//6+(cSW*uC+xSpeed), cSH*2//5+(cSH*uR+ySpeed), fill="burlywood1", width=0)
    canvas.create_rectangle(cSW*7//24+(cSW*uC+xSpeed),cSH//8+(cSH*uR+ySpeed), \
        cSW*9//24+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), fill="gold2", width=0)
    canvas.create_arc(cSW//3+(cSW*uC+xSpeed), cSH//10+(cSH*uR+ySpeed), \
        cSW*4//6+(cSW*uC+xSpeed), cSH*3//10+(cSH*uR+ySpeed), start=0, fill="gold2", \
        style=PIESLICE, outline="gold2")
    canvas.create_arc(cSW//3+(cSW*uC+xSpeed), cSH//10+(cSH*uR+ySpeed), \
        cSW*4//6+(cSW*uC+xSpeed), cSH*3//10+(cSH*uR+ySpeed), start=90, \
        fill="gold2", style=PIESLICE, outline="gold2")
    canvas.create_oval(cSW*11//20+(cSW*uC+xSpeed), cSH//5+(cSH*uR+ySpeed), \
        cSW*12//20+(cSW*uC+xSpeed), cSH//4+(cSH*uR+ySpeed), fill="black")
    points = ((cSW//2+(cSW*uC+xSpeed), cSH*2//5+(cSH*uR+ySpeed)), \
        (cSW//3+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed)), (cSW*2//3+(cSW*uC+xSpeed), \
        cSH*3//4+(cSH*uR+ySpeed)))
    canvas.create_polygon(points, fill="light coral")
    canvas.create_arc(cSW*11//20+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), \
        cSW*13//20+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), start=180, \
        style=ARC, outline="red3")
    points = ((cSW*10//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed)), \
        (cSW*11//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed)), \
        (cSW*12//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed)),(cSW*11//20+(cSW*uC+xSpeed), \
        cSH//2+(cSH*uR+ySpeed)))
    canvas.create_polygon(points, fill="navy")
    canvas.create_rectangle(cSW*10//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), \
        cSW*11//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed), fill="navy", width=0)
    canvas.create_rectangle(cSW*12//24+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed), \
        cSW*14/24+(cSW*uC+xSpeed), cSH*7//8+(cSH*uR+ySpeed), fill="LightCyan2", width=0)
    canvas.create_oval(cSW*12//24+(cSW*uC+xSpeed), cSH*13//16+(cSH*uR+ySpeed), \
        cSW*14/24+(cSW*uC+xSpeed), cSH*14//16+(cSH*uR+ySpeed), fill="black")

def drawCharElevenLeft(canvas, cSW, cSH, uR, uC, xSpeed=0, ySpeed=0):
    canvas.create_oval(cSW//3+(cSW*uC+xSpeed), cSH//8+(cSH*uR+ySpeed), \
        cSW*4//6+(cSW*uC+xSpeed), cSH*2//5+(cSH*uR+ySpeed), fill="burlywood1", width=0)
    canvas.create_rectangle(cSW*15//24+(cSW*uC+xSpeed),cSH//8+(cSH*uR+ySpeed), \
        cSW*17//24+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), fill="gold2", width=0)
    canvas.create_arc(cSW//3+(cSW*uC+xSpeed), cSH//10+(cSH*uR+ySpeed), 
        cSW*4//6+(cSW*uC+xSpeed), cSH*3//10+(cSH*uR+ySpeed), start=0, fill="gold2", \
        style=PIESLICE, outline="gold2")
    canvas.create_arc(cSW//3+(cSW*uC+xSpeed), cSH//10+(cSH*uR+ySpeed), \
        cSW*4//6+(cSW*uC+xSpeed), cSH*3//10+(cSH*uR+ySpeed), start=90, fill="gold2", \
        style=PIESLICE, outline="gold2")
    canvas.create_oval(cSW*4//10+(cSW*uC+xSpeed), cSH//5+(cSH*uR+ySpeed), \
        cSW*9//20+(cSW*uC+xSpeed), cSH//4+(cSH*uR+ySpeed), fill="black")    
    points = ((cSW//2+(cSW*uC+xSpeed), cSH*2//5+(cSH*uR+ySpeed)), (cSW//3+(cSW*uC+xSpeed), \
        cSH*3//4+(cSH*uR+ySpeed)), (cSW*2//3+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed)))
    canvas.create_polygon(points, fill="light coral")
    canvas.create_arc(cSW*7//20+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), \
        cSW*9//20+(cSW*uC+xSpeed), cSH//3+(cSH*uR+ySpeed), start=180, style=ARC, \
        outline="red3")  
    points = ((cSW*11//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed)), \
        (cSW*12//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed)), (cSW*13//20+(cSW*uC+xSpeed), \
        cSH*6//10+(cSH*uR+ySpeed)),(cSW*12//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed)))
    points = ((cSW*10//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed)), (cSW*9//20+(cSW*uC+xSpeed), \
        cSH*6//10+(cSH*uR+ySpeed)), (cSW*8//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed)), \
        (cSW*9//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed)))
    canvas.create_polygon(points, fill="navy")
    canvas.create_rectangle(cSW*9//20+(cSW*uC+xSpeed), cSH//2+(cSH*uR+ySpeed), \
        cSW*10//20+(cSW*uC+xSpeed), cSH*6//10+(cSH*uR+ySpeed), fill="navy", width=0)
    canvas.create_rectangle(cSW*11//24+(cSW*uC+xSpeed), cSH*3//4+(cSH*uR+ySpeed), \
        cSW*13/24+(cSW*uC+xSpeed), cSH*7//8+(cSH*uR+ySpeed), fill="LightCyan2", width=0)
    canvas.create_oval(cSW*11//24+(cSW*uC+xSpeed), cSH*13//16+(cSH*uR+ySpeed), \
        cSW*13/24+(cSW*uC+xSpeed), cSH*14//16+(cSH*uR+ySpeed), fill="black")