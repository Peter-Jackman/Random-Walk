from random import *
from turtle import *

#set up turtle
wn=Screen()
wn.bgcolor("black")
wn.title("Manhattan")
color('white')
speed(0)
penup()
goto(-200,200)
pendown()
hideturtle()

def man_walk():
    #define variables
    color('white')
    goto(-200,200)
    setheading(0)
    pendown()
    i=0
    j=0
    walk=[]
    coord={}
    showturtle()

    #if file exists, loads dict from file otherwise makes dict
    try:
        coord=eval(open("Times Visited.txt").read())
    except FileNotFoundError:
        coord={}
    
    #create dictionary of all points
        for z in range(0,7):
            for w in range(0,9):
                if (z,w) in coord:
                    continue
                else:
                    coord[(z,w)]=0

    #walk loop to (6,8)      
    while (i!=6 or j!=8):
        x=randint(1,2)
        if x==1:
            if i==0:
                a=randint(0,1)
                i+=a
                
                goto(-200+j*50,200-i*50)
            elif i==6:
                a=randint(-1,0)
                i+=a
                
                goto(-200+j*50,200-i*50)
            else:
                a=randint(-1,1)
                i+=a
                
                goto(-200+j*50,200-i*50)

        else:
            if j==0:
                a=randint(0,1)
                j+=a
                
                goto(-200+j*50,200-i*50)
                
            elif j==8:
                a=randint(-1,0)
                j+=a
                
                goto(-200+j*50,200-i*50)
            
            else:
                a=randint(-1,1)
                j+=a
                
                goto(-200+j*50,200-i*50)

        walk.append([i,j])

    #turns list of lists into tuple of tuples    
    route=[]
    for x in walk:
        route.append(tuple(x))
    route=tuple(route)
    
    #records number of times each junction was visited to dict
    for x in route:
        coord[x]+=1
                   
    #saves file with times visited
    with open('Times Visited.txt', 'w') as f:
        print(coord, file=f)

#draw a square of correct size
def draw_square():
    color('yellow')
    penup()
    goto(-200,200)
    pendown()
    forward(50*8)
    right(90)
    forward(50*6)
    right(90)
    forward(50*8)
    right(90)
    forward(50*6)
    right(90)

#fill square with dots
def draw_dots():
    for i_value in range(0,7):
        for j_value in range(0,9):
            speed(0)
            i_point=200-(i_value*50)
            j_point=-200+(j_value*50)
            penup()
            goto(j_point,i_point)
            dot(10,'green')


draw_square()
draw_dots()
man_walk()
