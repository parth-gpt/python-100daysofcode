import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- WORD DISPLAY ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")

data_list = data.to_dict(orient='records')
current_card = {}


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    fr_word = current_card["French"]
    canvas.itemconfig(lang_name, text="French", fill="black")
    canvas.itemconfig(lang_text, text=f"{fr_word}", fill="black")
    canvas.itemconfig(img, image=card_front)
    flip_timer = window.after(3000, func=flip)


# ---------------------------- CARD FLIP ------------------------------- #
def flip():
    en_word = current_card["English"]
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(lang_name, text="English", fill="white")
    canvas.itemconfig(lang_text, text=en_word, fill="white")


def is_known():
    data_list.remove(current_card)
    new_card()

    left_data = pandas.DataFrame(data_list)
    left_data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash-Learn")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
img = canvas.create_image(400, 261, image=card_front)
lang_name = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
lang_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="./images/right.png")
button = Button(image=right, highlightthickness=0, command=is_known)
button.grid(row=1, column=1)

wrong = PhotoImage(file="./images/wrong.png")
button = Button(image=wrong, highlightthickness=0, command=new_card)
button.grid(row=1, column=0)

new_card()

window.mainloop()
