import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S State Game")
image="us-states-game\states.gif"
screen.addshape(image)

turtle.shape(image)
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("us-states-game/50_states.csv")
all_states=data.state.tolist()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 Guessed",prompt="What's another state's name").title()
    if answer_state=="Exit":
        break
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
not_guessed=[]
for state in all_states:
    if state not in guessed_states:
        not_guessed.append(state)
data_dict={
    "not guessed":not_guessed,
    
}  
df=pandas.DataFrame(data_dict)
df.to_csv("us-states-game/learn.csv")


