import turtle
import random
t = turtle.Turtle()
t.speed(5)
def drawsquare():
    t.hideturtle()
    t.speed(0)
    d = 100
    t.speed(0)
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(90)
    t.forward(d)
    t.right(90)  
def one():
    t.reset()
    t.hideturtle()
    t.speed(0)
    d=100
    drawsquare()
    t.penup()
    t.forward(40)
    t.right(90)
    t.forward(d/2)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()
    t.pendown()
def two():
    t.reset()
    t.hideturtle()
    t.speed(0)
    drawsquare()
    d=100
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(d/2)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()
    t.home()
    t.forward(60)
    t.right(90)
    t.forward(d/2)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill() 
    t.penup()
    t.pendown()
def three():
 t.reset()
 t.hideturtle()
 t.speed(0)
 drawsquare()
 t.penup()
 t.forward(20)   
 t.right(90)
 t.forward(30)  #*
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 t.forward(60)
 t.right(90)
 t.forward(30)    #*
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 t.forward(40)
 t.right(90)
 t.forward(70)
 t.begin_fill()
 t.circle(10)
 t.end_fill()
 t.penup()
 t.pendown()
def four():
 t.reset()
 t.hideturtle()
 t.speed(0)
 drawsquare()
 t.penup()
 t.forward(20)
 t.right(90)
 t.forward(20)
 t.pendown()
 t.begin_fill()
 t.circle(8) 
 t.end_fill()#dot1
 t.penup()
 t.forward(50)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()#dot2
 t.penup()
 t.home()
 t.forward(65)
 t.right(90)
 t.forward(20)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill() 
 t.penup()
 t.forward(50)
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.pendown()
def five(): 
 t.reset()
 t.hideturtle()
 t.speed(0)
 drawsquare()
 t.penup()
 t.forward(20)
 t.right(90)
 t.forward(20)
 t.pendown()
 t.begin_fill()
 t.circle(8) 
 t.end_fill()#dot1
 t.penup()
 t.forward(50)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()#dot2
 t.penup()
 t.home()
 t.forward(65)
 t.right(90)
 t.forward(20)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill() 
 t.penup()
 t.forward(50)
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 t.forward(45)
 t.right(90)
 t.forward(45)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.pendown()
def six():
 t.reset()
 t.hideturtle()
 t.speed(0)
 drawsquare()
 t.penup()
 t.forward(10)
 t.right(90)
 t.forward(30)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.forward(40)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 # end of first two dots
 t.forward(40)
 t.right(90)
 t.forward(30)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.forward(40)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 # end of second two dots
 t.forward(70)
 t.right(90)
 t.forward(30)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill() 
 t.penup()
 t.forward(40)
 t.pendown()
 t.begin_fill()
 t.circle(8)
 t.end_fill()
 t.penup()
 t.home()
 t.penup()
 t.pendown()
dice = [1,2,3,4,5,6]
while(1<100):
    c = input("ROll? Enter Y or N \n")
    c = c.upper()
    if(c=="Y"):
        t.clear()
        t.reset()
        t.left(90)
        n = int(random.choice(dice))
        if(n==1):
            one()
        elif(n==2):
            two()
        elif(n==3):
            three()
        elif(n==4):
            four()
        elif(n==5):
            five()
        elif(n==6):
            six()
    if(c=="N"):
        print("THANK YOU!")
        break
t.bye()

