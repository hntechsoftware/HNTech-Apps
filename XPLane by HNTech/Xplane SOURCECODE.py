import turtle as t
import random
import time


# Create a turtle screen object
screen = t.Screen()
t.bgpic("src/bg.png")

#Initialize Window
screen.title("XPlane: HNTech")
screen.bgcolor("#adfffe")
screen.setup(770,370)

#Initialize variables
score = 0

#Initialize characters

jet = t.Turtle()
screen.addshape("src/jetchar.gif")
jet.shape("src/jetchar.gif")
jet.penup()
jet.backward(200)

def move_up():
    jet.setheading(90)
    jet_y = jet.ycor()
    if jet_y < 140:
        jet.forward(10)
        
def move_down():
    jet.setheading(270)
    jet_y = jet.ycor()
    if jet_y > -140:
        jet.forward(10)


# Bind the arrow keys to the functions to move the turtle up and down
t.onkeypress(move_up, "Up")
t.onkeypress(move_down, "Down")
t.onkeypress(move_up, "w")
t.onkeypress(move_down, "s")
t.listen()

#Define missle
missle = t.Turtle()
screen.addshape("src/missle.gif")
missle.shape("src/missle.gif")
missle.penup()
missle.setpos(250,0)
missle.speed(3)
missle.setheading(180)
time.sleep(1)

#Define scoreboard
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(200,100)
pen.write("Your score appears here", align="center",font=("candara", 16, "bold"))

def relocatemissle():
    choices = [1,2,3]
    coinflip = random.choice(choices)
    if coinflip != 1:
        missle.hideturtle()
        ycor = random.randint(-100,100)
        missle.setpos(250,ycor)
        missle.showturtle()
    else:
        missle.hideturtle()
        ycor = jet.ycor()
        missle.setpos(250,ycor)
        missle.showturtle()

def gameover():
    jet.hideturtle()
    missle.hideturtle()
    pen.clear()
    pen.write("Game Over", align="center",font=("candara", 16, "bold"))
    t.done()


def check_collision():
    if jet.distance(missle) < 40:
        return True
        
#Forever loop
while True:
    missle.forward(10)
    if check_collision():
        gameover()
        break
    if missle.xcor() < -400:
        relocatemissle()
        score = score + 1
        pen.clear()
        pen.write(score, align="center",font=("candara", 16, "bold"))





# Keep the turtle window open

