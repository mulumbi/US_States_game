import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = Turtle()
writer.hideturtle()
writer.penup()
# reading the csv data
data = pandas.read_csv("50_states.csv")
states = data.state
state_list = states.tolist()
# x_cords = data.x
# x_list = x_cords.tolist()
# y_cords = data.y
# y_list = y_cords.tolist()
score = 0
total = 50
named = []
while score != total:
    answer = screen.textinput(title= f"{score} / {total} States", prompt = "What a State name?").title()
    # check if answer is a valid state
    if answer in state_list and answer not in named:
        named.append(answer)
        state_data = data[data.state == answer]
        # write the state name at the x, y coord
        writer.goto(int(state_data.x), int(state_data.y))
        writer.pendown()
        writer.write(answer)
        writer.penup()
        score += 1
    else:
        # display error and loop again
        pass

screen.title(f"Great job! Your final score is {score} / {total}")
screen.exitonclick()