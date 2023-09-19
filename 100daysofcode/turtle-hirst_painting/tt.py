import turtle as t
import random as r

tim= t.Turtle()
t.colormode(255)

# #for drawing square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# #for dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

color =['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
#draw shapes with random colors 
# def draw_shapes(num_sides):
#     angle=360/num_sides
#     tim.color(r.choice(color))
#     for j in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for i in range(3,11):
#     draw_shapes(i)

#to draw randow way 
def random_color():
    rb=r.randint(0,255)
    g=r.randint(0,255)
    b=r.randint(0,255)
    random_color=(rb,g,b)
    return random_color

# degree=[90,180,270,360]
# for i in range(100):
#     tim.speed(100)
#     tim.width(5)
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(r.choice(degree)) 

#draw a spirograph
tim.speed("fastest")
ran=100


def spirograph(size):
    for i in range(0,int(360/size)):
        tim.setheading(tim.heading()+size)
        tim.color(random_color())
        tim.circle(ran)
        tim.tilt(5)

spirograph(5)
screen=t.Screen()
screen.exitonclick()