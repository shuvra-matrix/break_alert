from tkinter import *
import math
from playsound import playsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
rounds = 0
timer = None


def time_reset():
    global rounds
    button_sound()
    window.after_cancel(timer)
    label_1.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text="00:00")
    rounds = 0
    label_2.config(text="")


def start_time():
    global rounds
    rounds += 1
    if rounds == 1:
        button_sound()
    work_time = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    if rounds % 8 == 0:
        minimize_sound()
        window.state("zoomed")
        countdown(long_break)
        label_1.config(text="Break", fg=RED)
    elif rounds % 2 == 0:
        minimize_sound()
        window.state("zoomed")
        countdown(short_break)
        label_1.config(text="Break", fg=PINK)
    else:
        if rounds > 1:
            minimize_sound()
            window.state("zoomed")
        countdown(work_time)
        label_1.config(text="Work", fg=GREEN)


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 55 and minutes == 29:
        minimize_sound()
        window.iconify()

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(canvas_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks = " "
        sessions = math.floor(rounds / 2)
        for _ in range(sessions):
            marks = "✔"
        label_2.config(text=marks)


def button_sound():
    playsound("button.mp3")


def minimize_sound():
    playsound("minimize.mp3")


window = Tk()
window.title("Pomodoro")
window.maxsize(470, 410)
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
images = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=images)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label_1 = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
label_1.grid(row=1, column=2)

label_2 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_2.grid(row=4, column=2)

button_1 = Button(text="Strat", command=start_time)
button_1.grid(row=3, column=1)

button_2 = Button(text="Reset", command=time_reset)
button_2.grid(row=3, column=3)

window.mainloop()
