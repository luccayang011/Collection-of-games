from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_counting_down = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_counting_down)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text='Timer',fg=GREEN)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 ==0:
        #if it's the 8th repetition
        count_down(long_break_sec)
        timer.config(text='Break', fg=RED)
    elif reps % 2 ==0:
        #if it's the 2nd/4th/6th repetition
        count_down(short_break_sec)
        timer.config(text='Break', fg=PINK)
    else:
        # if it's the 1st/3rd/5th/7th repetition
        count_down(work_sec)
        timer.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    second = count % 60
    if second < 10:
        second = f"0{second}" # dynamic typing, change the data type for the same variable
    canvas.itemconfig(timer_text, text=f"{min}:{second}") # change a certain configuration in the timer has to use itemconfig()
    if count > 0:
        global timer_counting_down
        timer_counting_down = window.after(1000, count_down, count - 1)#wait for certain ms, and then execute the function
    else:
        start_timer()
        marks = ''
        num_checks = math.floor(reps / 2)
        for _ in range(num_checks):
            marks += '✔'
            checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#create the tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')  # read an image file
canvas.create_image(100, 112, image=tomato_img) # place the image in the center
timer_text = canvas.create_text(100, 132, text='00:00', fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1) # if didn't use it, the image will not show


#create labels
timer = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold"))
timer.grid(row=0,column=1)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=3)

#create buttons
start = Button(text="Start", highlightthickness=0, command=start_timer)
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)

start.grid(column=0, row=2)
reset.grid(column=2, row=2)



window.mainloop()
