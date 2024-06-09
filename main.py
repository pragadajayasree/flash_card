from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIMER = "0"

try:
    data = pandas.read_csv("data/new_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/data.csv")
    data_dict = {row.HINDI: row.ENGLISH for (index, row) in data.iterrows()}
else:
    data_dict = {row.HINDI: row.ENGLISH for (index, row) in data.iterrows()}


# hindi = [i for i in hindi.values()]
# english = data_dict["ENGLISH"]
# english = [i for i in english.values()]

def time():
    global TIMER
    TIMER = window.after(3000, back, back_img, eng_word)


def click():
    global eng_word, hin_word
    new_word = random.choice(list(data_dict))
    canvas.itemconfig(lang, text="Hindi")
    canvas.itemconfig(word, text=new_word)
    eng_word = data_dict[new_word]
    hin_word = new_word
    time()


def right():
    del data_dict[hin_word]
    new_data = pandas.DataFrame(list(data_dict.items()), columns=["HINDI", "ENGLISH"])
    new_data.to_csv("data/new_words_to_learn.csv")
    click()


def back(new_img, new_eng_word):
    global TIMER
    canvas.itemconfig(image, image=new_img)
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=new_eng_word, fill="white")
    window.after_cancel(TIMER)


window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

lang = canvas.create_text(400, 150, text="Hindi", font=("Ariel", 40, "bold"))
hin_word = random.choice(list(data_dict))
eng_word = data_dict[hin_word]

word = canvas.create_text(400, 263, text=hin_word, font=("Ariel", 50, "bold"))

time()

wrong_img = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_img, highlightthickness=0, command=click)
button1.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
button2 = Button(image=right_img, highlightthickness=0, command=right)
button2.grid(row=1, column=1)

window.mainloop()
