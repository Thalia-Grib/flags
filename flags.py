import turtle
import random
bob = turtle.Turtle()
points=0
lives=3

sam=turtle.Turtle()
scn= turtle.Screen()


def Germany():

    sam.fillcolor("black")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0,-50)
    sam.fillcolor("red")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0,-100)
    sam.fillcolor("yellow")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

def Italy():

    sam.fillcolor("green")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(50,0)
    sam.fillcolor("white")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(100, 0)
    sam.fillcolor("red")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()


def France():

    sam.fillcolor("blue")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(50,0)
    sam.fillcolor("white")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(100, 0)
    sam.fillcolor("red")
    sam.pendown()
    sam.begin_fill()
    for i in range(2):
        sam.forward(50)
        sam.right(90)
        sam.forward(150)
        sam.right(90)

    sam.end_fill()
    sam.penup()

def Russia():
    sam.fillcolor("white")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0, -50)
    sam.fillcolor("blue")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0, -100)
    sam.fillcolor("red")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(50)
        sam.right(90)

    sam.end_fill()
    sam.penup()

def Poland():
    sam.fillcolor("white")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(70)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0, -70)
    sam.fillcolor("red")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(70)
        sam.right(90)

    sam.end_fill()
    sam.penup()


def Sweden():
    sam.fillcolor("blue")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(140)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(50,0)
    sam.fillcolor("yellow")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(20)
        sam.right(90)
        sam.forward(140)
        sam.right(90)

    sam.end_fill()
    sam.penup()

    sam.goto(0, -50)
    sam.fillcolor("yellow")
    sam.pendown()
    sam.begin_fill()

    for i in range(2):
        sam.forward(200)
        sam.right(90)
        sam.forward(20)
        sam.right(90)

    sam.end_fill()
    sam.penup()

def Ireland():
    sam = turtle.Turtle()
    sam.speed(2)
    sam.pencolor("black")

    sam.fillcolor("green")
    sam.begin_fill()
    sam.penup()
    sam.goto(-25, -70)
    sam.pendown()
    sam.goto(-25, -70)
    sam.goto(-75, -70)
    sam.goto(-75, -200)
    sam.goto(-25, -200)
    sam.goto(-25, -70)
    sam.end_fill()

    sam.fillcolor("black")
    sam.begin_fill()
    sam.goto(25, -70)
    sam.goto(25, -200)
    sam.goto(-25, -200)

    sam.fillcolor("orange")
    sam.begin_fill()
    sam.penup()
    sam.goto(25, -70)
    sam.pendown()
    sam.goto(75, -70)
    sam.goto(75, -200)
    sam.goto(25, -200)
    sam.goto(25, -70)
    sam.end_fill()

def Rumania():
    sam = turtle.Turtle()
    sam.speed(2)
    sam.pencolor("black")

    sam.fillcolor("blue")
    sam.begin_fill()
    sam.penup()
    sam.goto(-25, -70)
    sam.pendown()
    sam.goto(-25, -70)
    sam.goto(-75, -70)
    sam.goto(-75, -200)
    sam.goto(-25, -200)
    sam.goto(-25, -70)
    sam.end_fill()

    sam.fillcolor("yellow")
    sam.begin_fill()
    sam.goto(25, -70)
    sam.goto(25, -200)
    sam.goto(-25, -200)
    sam.end_fill()

    sam.fillcolor("red")
    sam.begin_fill()
    sam.penup()
    sam.goto(25, -70)
    sam.pendown()
    sam.goto(75, -70)
    sam.goto(75, -200)
    sam.goto(25, -200)
    sam.goto(25, -70)
    sam.end_fill()

def Belgium():
    sam = turtle.Turtle()
    sam.speed(2)
    sam.pencolor("black")

    sam.fillcolor("black")
    sam.begin_fill()
    sam.penup()
    sam.goto(-25, -70)
    sam.pendown()
    sam.goto(-25, -70)
    sam.goto(-75, -70)
    sam.goto(-75, -200)
    sam.goto(-25, -200)
    sam.goto(-25, -70)
    sam.end_fill()

    sam.fillcolor("yellow")
    sam.begin_fill()
    sam.goto(25, -70)
    sam.goto(25, -200)
    sam.goto(-25, -200)
    sam.end_fill()

    sam.fillcolor("red")
    sam.begin_fill()
    sam.penup()
    sam.goto(25, -70)
    sam.pendown()
    sam.goto(75, -70)
    sam.goto(75, -200)
    sam.goto(25, -200)
    sam.goto(25, -70)
    sam.end_fill()


countries= [Germany , Italy , France, Russia , Poland , Sweden , Ireland , Rumania , Belgium ]


while lives > 0 and len(countries) > 0:
    sam.reset()
    flag = random.choice(countries)
    flag()
    answer = input("Guess the flag!!")
    if answer == flag.__name__:
        print("Correct")
        points =  points +1
        countries.remove(flag)
        sam.reset()
    else:
        print("Incorrect")
        lives = lives -1
        sam.reset()

    print("points: ",points)
    print("lives: ",lives)

if points >7:
    print("Perfect score ")
elif points >5:
    print("good score ")
elif points <5:
    print("bad score ")


turtle.done()