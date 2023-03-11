import turtle
import random


def obj (shape,h,w,col,x,y):  # create turtle object
    ob =turtle.Turtle()
    ob.speed(0)
    ob.shape(shape)
    ob.shapesize(h,w)
    ob.color(col)
    ob.penup()
    ob.goto(x,y)
    return ob

def MSG_obj (string,col,size,x,y): # create turtle object as a Message
    msg = turtle.Turtle()
    msg.speed(0)
    msg.penup()
    msg.hideturtle()
    msg.color(col)
    msg.goto(x,y)
    msg.write(f"{string}" , align="center",font=("Courier",size,"normal"))
    return msg

def rand_goal(): # get random postion for the goal
    while True:
        g =random.randint(1,115)
        if g!=53 and g!=63:
            return g


#Screen
wind = turtle.Screen()
wind.title("Dot Maze")
wind.setup(height=610,width=810)
wind.bgcolor("#000000")
wind.tracer(0)
wind.listen()

cnt=0
rand= rand_goal()
DOTs = {}
winner = None

for y in range(-5,6): # create the maze with players and goal
    for x in range(-5,6-(y%2)):
        posX =(x*80)+(40*(y%2))
        posY =y*60
        cnt+=1
        
        if cnt ==53:
            blue = obj("square",1.2,1.2,"#00a8e8",posX,posY)
            bluepos = blue.pos()
        elif cnt == 63:
            red = obj("square",1.2,1.2,"#d90429",posX,posY)
            redpos = red.pos()
        elif cnt== rand:
            goal=obj("turtle",1.5,1.5,"#8ac926",posX,posY)
        else:
            dot = obj("circle",0.8,0.8,"#ffffff",posX,posY)
            DOTs.update({dot.pos():True})


#functions red
def red_up():
    red.sety(red.ycor()+20)
    if red.ycor() == 320:
        red.sety(-300)
    elif DOTs.get(red.pos()):
        red.goto(redpos)

def red_down():
    red.sety(red.ycor()-20)
    if red.ycor() == -320:
        red.sety(300)
    elif DOTs.get(red.pos()):
        red.goto(redpos)

def red_right():
    red.setx(red.xcor()+20)
    if red.xcor()==420:
        red.setx(-400)
    elif DOTs.get(red.pos()):
        red.goto(redpos)

def red_left():
    red.setx(red.xcor()-20)
    if red.xcor()==-420:
        red.setx(400)
    elif DOTs.get(red.pos()):
        red.goto(redpos)

# red keyboard keys    
wind.onkeypress(red_up,"Up")
wind.onkeypress(red_down,"Down")
wind.onkeypress(red_left,"Left")
wind.onkeypress(red_right,"Right")

#functions blue
def blue_up():
    blue.sety(blue.ycor()+20)
    if blue.ycor() == 320:
        blue.sety(-300)
    elif DOTs.get(blue.pos()):
        blue.goto(bluepos)

def blue_down():
    blue.sety(blue.ycor()-20)
    if blue.ycor() == -320:
        blue.sety(300)
    elif DOTs.get(blue.pos()):
        blue.goto(bluepos)

def blue_right():
    blue.setx(blue.xcor()+20)
    if blue.xcor()==420:
        blue.setx(-400)
    elif DOTs.get(blue.pos()):
        blue.goto(bluepos)

def blue_left():
    blue.setx(blue.xcor()-20)
    if blue.xcor()==-420:
        blue.setx(400)
    elif DOTs.get(blue.pos()):
        blue.goto(bluepos)
        
# blue keyboard keys
wind.onkeypress(blue_up,"w")
wind.onkeypress(blue_down,"s")
wind.onkeypress(blue_left,"a")
wind.onkeypress(blue_right,"d")


#main game loop
while True:
    wind.update()
    if red.pos()==goal.pos():
        winner = red
        break
    
    if blue.pos()==goal.pos():
        winner = blue
        break


loop = True
wind.clear()
wind.bgcolor("#000000")
MSG_obj("WINS",winner.color()[0],100,0,0)
MSG_obj("press SPACE to EXIT",winner.color()[0],20,0,-260)

def exit():
    global loop
    loop=False

wind.onkeypress(exit,"space")

while loop:
    wind.update()



    