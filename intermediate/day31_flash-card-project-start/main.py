from tkinter import *
from tkinter import Canvas

import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
words = {}
current_word = {}

# ____________Data upload_____________________________


try:
    data = pd.read_csv("data//words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data//french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")



# ______________Buttons_functionality_________________

def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words)
    canvas.itemconfig(language_text, text='French', fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(card_color, image=image_front)
    flip_timer = window.after(3000, change_side)

def right():
    words.remove(current_word)
    next_word()
    data = pd.DataFrame(words)
    data.to_csv("data//words_to_learn.csv", index=False)

# ____________Card changing functionality______________


def change_side():
    canvas.itemconfig(card_color, image=image_back)
    canvas.itemconfig(language_text, text='English', fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    window.after_cancel(flip_timer)


# _______________UI setup______________________________
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, change_side)

# Cards setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_front = PhotoImage(file="images//card_front.png")
image_back = PhotoImage(file="images//card_back.png")
card_color = canvas.create_image(400, 263, image=image_front)
canvas.grid(column=0, row=0, columnspan=2)

# Text setup
language_text = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0)
word_text = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0)

# Buttons setup
right_image = PhotoImage(file="images//right.png")
wrong_image = PhotoImage(file="images//wrong.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(column=1, row=1)

next_word()

window.mainloop()
