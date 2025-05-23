import tkinter

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
to_ignore = []
current_card = {}


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(canvas_image, image = flash_card_back)
    canvas.itemconfig(language,text="English")
    canvas.itemconfig(word, text =current_card["English"])




def next_card():
    global current_card, flip_timer
    canvas.itemconfig(canvas_image, image=flash_card_front)
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language,text="French")
    canvas.itemconfig(word,text=current_card["French"])
    flip_timer = window.after(3000,func=flip_card)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg="#B1DDC6")
flip_timer = window.after(3000, func=flip_card)


# --- Canvas ---
flash_card_front = PhotoImage(file = "images/card_front.png")
flash_card_back = PhotoImage(file = "images/card_back.png")
canvas = Canvas(width=800,height=526)
canvas_image = canvas.create_image(400,263, image= flash_card_front)
language =canvas.create_text(400,150, text = "", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text = "", font=("Ariel", 60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)


# --- Buttons ---- #

right_image=PhotoImage(file = "images/right.png")
wrong_image=PhotoImage(file = "images/wrong.png")


right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button= Button(image=wrong_image, highlightthickness=0, command=next_card)

right_button.grid(row=1, column = 1)
wrong_button.grid(row=1,column = 0)



next_card()

tkinter.mainloop()