import turtle
import random

myTurtle=turtle.Turtle()
myTurtle.speed(20)
#a function is a block of code that has it's own name and it can be called multiple times
def drawsquare(side):
    """this function draws a square"""
    for i in range(4):
        myTurtle.forward(side)
        myTurtle.left(90)
   
def drawhouse(side):
    """this function draws a house"""
    for i in range(4):
        myTurtle.forward(side)
        myTurtle.left(90)
    myTurtle.left(135)
    myTurtle.forward(side)
    myTurtle.right(90)
    myTurtle.forward(side)
    myTurtle.right(135)
    myTurtle.forward(side)

def drawstriangle(side):
    """this function draws a triangle"""
    for  i in range(3):
        myTurtle.forward(side)
        myTurtle.left(120)
   

def drawrectangle(sideA,sideB):
    """this function draws a rectangle"""
    for i in range(2):
        myTurtle.forward(sideA)
        myTurtle.left(90)
        myTurtle.forward(sideB)
        myTurtle.left(90)

def moveturtle(x,y):
    """this function moves the pencil to another place"""
    myTurtle.up()
    myTurtle.goto(x,y)
    myTurtle.down()

def generatesquaredata(
        startx,
        endx,
        starty,
        endy,
        side):
    """this function generates random data for squares"""
    #a list for data
    squaredata=[]
    #in the cycle we generate data for the squares
    for i in range(10):
        x=random.randint(startx,endx)
        y=random.randint(starty,endy)
        randomside=random.randint(10,side)
        squaredata.append([x,y,randomside])
    return squaredata

def drawtriangles():
    """in the loop are drawn triangles"""
    for cordinate in squarecordinates:
        x,y,side=cordinate
        myTurtle.color(random.choice(colours))
        drawstriangle(side)
        moveturtle(x,y)

def drawtriangleflower():
    myTurtle.width(4)
    for i in range(21):
        myTurtle.color(random.choice(colours))
        drawstriangle(side=50)
        myTurtle.left(15)

def drawstar(length,colour):
    for i in range(5):
        myTurtle.color(colour)
        myTurtle.forward(length)
        myTurtle.left(144)
#drawstar(length=100,colour="yellow")

colours=["blue","green","orange","red","#22E8FA","#060270"]


squarecordinates=generatesquaredata(
    startx=-300,
    endx=300,
    starty=-300,
    endy=300,
    side=40
)

print(squarecordinates)

coordinates=[
        [230, 5],
        [0,200],
        [-200,-100]
    ]

for coordinate in coordinates:
    """it unpackeds the list"""
    x,y=coordinate
    drawtriangleflower()
    moveturtle(x,y)
    drawstar(length=100,colour="orange")

# drawsquare(50)
# moveturtle(-200,-200)
# drawsquare(20)
# moveturtle(-200,200)
# drawsquare(10)
# moveturtle(-200,100)
# drawrectangle(20,50)

myTurtle.screen.mainloop()