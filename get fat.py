import turtle
import time
import random
delay=0.1
score=0
high_score=0
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,100)
head.direction='stop'

win = turtle.Screen()
win.title("turtle game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+5)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-5)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+5)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-5)



def go_up():
    if head.direction != "down":
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def home():
    head.home()


win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
win.onkey(home, "h")


food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50,0.50)
food.goto(0,0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0  High Score : 0", align="center",font=("candara", 24, "bold"))


segments=[]



while True:
    win.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        colors=random.choice(['red','blue','green'])
        shapes=random.choice(['square','circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        delay-0.1
        pen.clear()
        pen.write("Score: {} High Score:{}".format( score,high_score),align='center',font=("candara",24))
    if head.distance(food)< 15:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001
        score+=10
        if score>high_score:
                  high_score=score

        pen.clear()
        pen.write("Score:{} High score:{}".format(score,high_score),align="center",font=("candara",24))
                  
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    
    time.sleep(delay)
win.mainloop()
    

