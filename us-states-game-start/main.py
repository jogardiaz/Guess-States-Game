import turtle
import pandas

ALIGN = 'center'
FONT = ('courier', 10, 'normal')

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

game_on = True
score = 0
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
guessed_states = []
print(states)

while game_on:
    answer = screen.textinput(title=f'{score}/50 States Guessed', prompt='Whats the state?').title()
    if answer in states:
        score += 1
        states.remove(answer)
        guessed_states.append(answer)

        state = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer, align=ALIGN, font=FONT)
    elif answer == 'Exit':
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

        print(states)

