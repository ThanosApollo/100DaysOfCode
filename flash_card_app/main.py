from email.mime import image
from tkinter import *

background_color = "#B1DDC6"



##Window
window = Tk()
window.title('Flash Cards')
window.config(padx=30,pady=30,bg=background_color)




##Parts

canvas = Canvas(width=926,height=726)
card_front = PhotoImage(file='flash_card_app/images/card_front.png')
right_image = PhotoImage(file='flash_card_app/images/right.png')
canvas.create_image(465,360, image=card_front)
canvas.config(bg=background_color,highlightbackground=background_color)







##Grid Layout
canvas.grid(column=0,row=0,columnspan=2)







## 

window.mainloop()