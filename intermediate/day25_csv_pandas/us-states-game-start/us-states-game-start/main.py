import turtle

screen = turtle.Screen()
screen.title("States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What`s another state`s name")

print(answer_state)

screen.mainloop()