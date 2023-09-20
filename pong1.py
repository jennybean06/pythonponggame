import turtle

wn = turtle.Screen()
wn.title("Pong by Jenny")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0) #(x,y)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0) #(x,y)

#ball 
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) #(x,y)
ball.dx = 0.2 #delta x co-ordinate, every time the ball moves, it moves by 2px
ball.dy = 0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0 PlayerB: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def paddle_a_up():
    y = paddle_a.ycor() #get the y co-ordinate
    y += 20 #add 20px to the y
    paddle_a.sety(y) #set the y to the new y co-ordinate

def paddle_a_down():
    y = paddle_a.ycor() #get the y co-ordinate
    y -= 20 #subtract 20px to the y
    paddle_a.sety(y) #set the y to the new y co-ordinate

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20 
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20 
    paddle_b.sety(y) 


#Keyboard binding
wn.listen ()#tells it to listen to keyboard input
wn.onkeypress(paddle_a_up, "w") #when the user presses w, call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") #when the user presses s, call the function paddle_a_down
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down") 





#main game loop
while True:
    wn.update()

#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#border checking, for the top border
    if ball.ycor() > 290:
     ball.sety(290)
     ball.dy *= -1 #if dy is 2 then it will reverse

#border checking, for the bottom border
    if ball.ycor() < -290:
     ball.sety(-290)
     ball.dy *= -1 

#border checking, for the right side
    if ball.xcor() > 390:
     ball.goto(0, 0)
     ball.dx *= -1 
     score_a +=1
     pen.clear()
     pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#border checking, for the left
    if ball.xcor() < -390:
     ball.goto(0, 0)
     ball.dx *= -1 
     score_b += 1
     pen.clear()
     pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


#paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
     ball.setx(340)
     ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
     ball.setx(-340)
     ball.dx *= -1