from turtle import Turtle

ALIGN = 'center'
FONT = ('courier', 15, 'normal')

class State(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        #self.hideturtle()
        self.penup()
        self.color('black')
        self.x = x
        self.y = y
        self.state = state
        self.write_state()


    def write_state(self):
        self.x.x
        self.y.y
        #self.goto(self.x, self.y)
        #self.write(f'{self.state}', align=ALIGN, font=FONT)