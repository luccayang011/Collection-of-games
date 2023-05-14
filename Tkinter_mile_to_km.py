from tkinter import *

def mile_to_km():
    output_label.config(text=round(float(input.get())*1.609,2))

window = Tk()  # need a way to keep the window on the screen
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)# add padding/space

# Label
miles = Label(text='Miles')
miles.grid(column=3, row=1)  # need to specify how we want to lay out this window
# my_label.config(padx=50, pady=50)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=1, row=2)

output_label = Label(text='0')
output_label.grid(column=2, row=2)

km = Label(text='Km')
km.grid(column=3, row=2)

# Entry
input = Entry(width=8)
input.grid(column=2, row=1)

# Button
button = Button(text='Calculate', command=mile_to_km)  # equals the name of the function, not run the function
button.grid(column=2, row=3)

window.mainloop()  # the line of code that keeps the window on the screen and listen to user's instructions
