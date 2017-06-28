from turtle import *

def get_number_of_corners():
    number = int(raw_input("how many sides are wanted, sir? "))
    return number

def get_angle(sides): 
    angle = 360 / sides
    return angle

def draw_shape_user_input_sides():
    sides = get_number_of_corners()
    angle = get_angle(sides)
    for i in range(sides):
        left(angle)
        forward(100)


def main():
    draw_shape_user_input_sides()
    mainloop()



main()
