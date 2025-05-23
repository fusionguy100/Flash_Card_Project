import tkinter

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import csv



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg="#B1DDC6")


# --- Canvas ---
flash_card_front = PhotoImage(file = "images/card_front.png")
flash_card_back = PhotoImage()
canvas = Canvas(width=800,height=526)
canvas.create_image(400,263, image= flash_card_front)
canvas.create_text(400,150, text = "Title", font=("Ariel", 40, "italic"))
canvas.create_text(400,263, text = "Word", font=("Ariel", 60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)



# --- Buttons ---
right_image=PhotoImage(file = "images/right.png")
wrong_image=PhotoImage(file = "images/wrong.png")


right_button = Button(image=right_image, highlightthickness=0)
wrong_button= Button(image=wrong_image, highlightthickness=0)

right_button.grid(row=1, column = 1)
wrong_button.grid(row=1,column = 0)

















tkinter.mainloop()