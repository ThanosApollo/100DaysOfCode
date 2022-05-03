from tkinter import *

window = Tk()
window.title('Miles to Kilometer')
window.minsize(width=300, height=100)




def convert_to_km():
    miles = miles_input.get() 
    miles = float(miles)
    km = miles * 1.609
    km_number_text.config(text=km)

## Components 

equal_label = Label(text='is equal to')

miles_input = Entry()
miles_text = Label(text='Miles')

km_number_text = Label(text='0')
kilometer_text = Label(text='Kilometers')

convert_button = Button(text='Convert', command=convert_to_km)



## Grid

equal_label.grid(column=0,row=1)
miles_input.grid(column=1,row=0)
miles_text.grid(column=2,row=0)
km_number_text.grid(column=1,row=1)
kilometer_text.grid(column=2,row=1)
convert_button.grid(column=1,row=2)


window.mainloop()
