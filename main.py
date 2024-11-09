from tkinter import *
import  math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REP = 1
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    if REP % 2 == 0:
        count_down(300)
    else:
        count_down(1500)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=f"{math.floor(count/60)}:{count%60}")
    if count > 0:
        window.after(1000, count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg="#E7D4B5")

canvas = Canvas(width=200, height=224, bg="#E7D4B5", highlightthickness=0)
timer = Label(text="Timer",fg=GREEN, bg= "#E7D4B5",font=(FONT_NAME,35,"bold"))
timer.grid(column=1, row=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)
reset = Button(text="Reset")
reset.grid(column=2,row=2)
tick = Label(text="✓",fg=GREEN, bg= "#E7D4B5",font=(FONT_NAME,35,"bold"))
tick.grid(column=1, row=3)

window.mainloop()
