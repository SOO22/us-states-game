import pandas
import turtle
from turtle import Turtle
FONT = ("Arial", 8, "normal")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    scribe = Turtle()
    scribe.hideturtle()
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states_list)} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in states_list if (state not in correct_guesses)]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = data[data.state == answer_state]
        xcor = int(state.x)
        ycor = int(state.y)
        scribe.penup()
        scribe.goto(xcor, ycor)
        scribe.write(answer_state, align="center", font=FONT)
        print(correct_guesses)

    # Automate correct answers
    # for state in states_list:
    #     correct_guesses.append(state)
    #     state_pos = data[data.state == state]
    #     xcor = int(state_pos.x)
    #     ycor = int(state_pos.y)
    #     scribe.penup()
    #     scribe.goto(xcor, ycor)
    #     scribe.write(state)
    #     print(correct_guesses)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

