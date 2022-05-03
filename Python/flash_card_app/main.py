from cgitb import text
from operator import index
from textwrap import fill
from tkinter import *
from turtle import title
import pandas 
import random
background_color = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv('flash_card_app/data/words_to_learn.csv')
except :
    data = pandas.read_csv('flash_card_app/data/bg_words.csv')
    
to_learn = data.to_dict(orient='records')

def is_known():
    global current_card
    to_learn.remove(current_card)
    words_data = pandas.DataFrame(to_learn)
    words_data.to_csv("flash_card_app/data/words_to_learn.csv",index=False)
    
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text='Bulgarian',fill='black')
    canvas.itemconfig(card_word,text=current_card['Bulgarian'],fill='black')
    canvas.itemconfig(background_image,image=card_front)
    flip_timer = window.after(3000, func=flip_card) 
    


def flip_card():
    canvas.itemconfig(background_image,image=card_back)
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word,text=current_card['English'],fill='white')

##Window
window = Tk()
window.title('Flash Cards')
window.geometry('1000x800')
window.config(padx=30,pady=30,bg=background_color)


flip_timer = window.after(3000, func=flip_card)

##Parts

canvas = Canvas(width=826,height=600)
card_front = PhotoImage(file='flash_card_app/images/card_front.png')
card_back = PhotoImage(file='flash_card_app/images/card_back.png')
right_image = PhotoImage(file='flash_card_app/images/right.png')
wrong_image = PhotoImage(file='flash_card_app/images/wrong.png')

background_image = canvas.create_image(430,320, image=card_front)
card_title = canvas.create_text(430,150,text='', font=("Ariel",30,"italic"),fill="black")
card_word = canvas.create_text(430,320, text='', font=("Ariel",60,"bold"),fill="black")
canvas.config(bg=background_color,highlightbackground=background_color)
right_button = Button(image=right_image, highlightbackground=background_color, command=is_known)
wrong_button = Button(image=wrong_image,highlightbackground=background_color, command=next_card)
question_label = Label()







##Grid Layout
canvas.grid(column=0,row=0,columnspan=2)
right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)



next_card()



## 

window.mainloop()