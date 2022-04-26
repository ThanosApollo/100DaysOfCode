from tkinter import *
from tkinter import messagebox
import random
import pyperclip

## Generate Password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



window = Tk()
window.title('Password Manager')
window.config(padx=10,pady=20)


## Functions

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
   
    
    
    if len(password) > 0 and len(website) > 0 and len(email) > 0: 
        is_ok = messagebox.askokcancel('Save Login info',f'Website:{website}:\nLogin: {email}\nPassword: {password}\n Do you want to save Login info?')
        if is_ok: 
            with open('password_manager/data.txt', 'a') as data_file:
                data_file.write(f'\n{website}|{email}|{password}')
                website_entry.delete(0, END)
                email_entry.delete(0, END)  
                password_entry.delete(0, END)
    else :
        messagebox.showinfo('ERROR', 'ERROR: Empty field')
          
    
    






## Parts

canvas = Canvas(width=300,height=300)
logo_image = PhotoImage(file='password_manager/logo2.png')
canvas.create_image(150,150,image=logo_image)

website_label = Label(text='Website:')
email_label = Label(text='Email/Username:')
password_label = Label(text='Password: ')

generate_password_button = Button(text='Generate Password', command=generate_password)
add_button = Button(text='Add', width=36, command=save)


website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=18)






## Grid Layout

canvas.grid(column=1,row=0)
website_label.grid(column=0,row=1)
website_entry.grid(column=1,row=1, columnspan=2)
email_label.grid(column=0,row=2)
email_entry.grid(column=1,row=2,columnspan=2)
password_label.grid(column=0,row=3)
password_entry.grid(column=1,row=3)
generate_password_button.grid(column=2,row=3)
add_button.grid(column=1,row=4, columnspan=2)




##

website_entry.focus()



window.mainloop()