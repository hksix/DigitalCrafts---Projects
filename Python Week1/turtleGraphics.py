from turtle import *

def center_turtle():
    up()
    forward(150)
    left(90)
    left(270)
    down()

def draw_a_square():
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)




def fly_turtle_fly():
    up()
    right(90)
    forward(150)
    down()

def draw_a_circle():
    # begin_fill()
    # fillcolor('red')
    pencolor('orange')
    width(1)
    circle(100)
    # end_fill()

def draw_a_star():
    for i in range(5):
        forward(125)
        right(144)

def draw_h():
    left(90)
    forward(100)
    up()
    right(180)
    forward(50)
    down()
    right(270)
    forward(50)
    up()
    left(90)
    forward(50)
    right(180)
    down()
    forward(100)

def draw_a():
    left(75)
    forward(100)
    right(150)
    forward(100)
    up()
    left(180)
    forward(50)
    down()
    left(75)
    forward(25)
    up()
    right(180)
    forward(60)
    right(90)
    forward(50)
    left(90)
def main():
    # center_turtle()
    # draw_a_circle()
    # up()
    # left(90)
    # forward(75)
    # down()
    # draw_a_star()
    # draw_a_square()
    # fly_turtle_fly()
    # draw_a_square()
    # draw_a_square()
    # draw_h()
    # draw_a()
    mainloop()

main ()