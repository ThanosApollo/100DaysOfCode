from tkinter import *
import random
import math
# ---------------------------- CONSTANTS ------------------------------- #
black = "#000000"
black_red = "#3D0000"
less_red = "#950101"
red = "#FF0000"
green = '#00FF00'
FONT_NAME = "Courier"
WORK_MIN = 35
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
quotes = ["Victorious warriors draw their strength\n from the highest source; their love.", 
          "Every warrior wants a worthy opponent.\n There is no redress in fighting the pathetic.", 
          "A warrior never worries about his fear.",
          "Victory are reserved for those warriors\n who are willing to pay it's price."]
checkmark_list = []


# ---------------------------- TIMER RESET ------------------------------- # 
def restart_time():
    window.after_cancel(timer)
    global reps
    global checkmark_list 
    reps = 0
    checkmark_list = []
    check_mark.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    
   

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text='Long Rest✅', font=(FONT_NAME, 35, 'bold'), fg=green)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text='Rest✅', font=(FONT_NAME, 35, 'italic'), fg=green)
    elif reps % 2 != 0:
        count_down(work_sec)
        random_quote = random.choice(quotes)
        timer_title.config(text=random_quote, font=(FONT_NAME, 20), fg=red)
    
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec == '00'
    elif count_sec < 10:
        count_sec = '0' + str(count_sec)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        
    else :
        start_timer()
        if reps % 2 == 0 :
            checkmark_list.append(check)
            check_mark.config(text=checkmark_list)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Warrior Time!')
window.config(padx=50,pady=100)







fg = '#00FF00'
check = '✔'
canvas = Canvas(width=510,height=525)
warrior_image = PhotoImage(file='pomodoro_timer/warrior_image.png')
canvas.create_image(260, 260, image=warrior_image)
timer_text = canvas.create_text(260,270, text="00:00", font=(FONT_NAME, 35, 'bold'),)




### Parts

start_button = Button(text='Start', command=start_timer)
check_mark = Label(fg=green)
reset_button = Button(text='Reset',bg=black, command=restart_time)
timer_title = Label(text='Fight time!', font=(FONT_NAME, 40), )








## Grid 
timer_title.grid(column=1,row=0)
canvas.grid(column=1,row=1)
start_button.grid(column=0,row=2)
check_mark.grid(column=1,row=2)
reset_button.grid(column=2,row=2)



window.mainloop()
