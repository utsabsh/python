import colorgram
import turtle as t
import random
# rgb_list=[]
# colors = colorgram.extract('turtle-hirst_painting\hirst-painting\img.jpg',30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_list.append(new_color)
# print(rgb_list)
t.colormode(255)
color=[(235, 236, 238), (231, 235, 232), (180, 66, 36), (212, 150, 97), (15, 25, 42), (239, 232, 236), (239, 209, 93), (234, 63, 34), (153, 27, 20), (72, 30, 33), (84, 92, 114), (67, 42, 36), (118, 33, 38), (160, 141, 71), (137, 153, 164), (177, 90, 99), (50, 52, 126), (157, 66, 71), 
(234, 169, 158), (168, 143, 149), (98, 115, 114), (15, 27, 27), (157, 165, 164), (220, 174, 179), (189, 189, 197), (75, 70, 46), (121, 122, 144), (187, 194, 189), (118, 132, 135)]
tt=t.Turtle()
tt.penup()
tt.hideturtle()
tt.speed("fastest")
tt.setheading(225)
tt.forward(300)
tt.setheading(0)
num=100
for i in range(1,num+1):
    tt.dot(20,random.choice(color))
    tt.forward(50)
    if i %10==0:
        tt.setheading(90)
        tt.forward(50)
        tt.setheading(180)
        tt.forward(500)
        tt.setheading(0)

screen=t.Screen()
screen.exitonclick()