from tkinter import *
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
CHECKMARK = "✔"
CHECKMARK_COUNTER = 0
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global REPS, CHECKMARK_COUNTER
    REPS = 0
    CHECKMARK_COUNTER = 0
    window.after_cancel(TIMER)
    label_13.config(text="")
    label_10.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS, CHECKMARK_COUNTER
    REPS += 1
    working_time = WORK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    if REPS % 8 == 0:
        countdown_time = long_break_time
        CHECKMARK_COUNTER = 0
        label_13.config(text="")
        label_10.config(text="Break", fg=RED)
        messagebox.showinfo(title="times up", message="its time for a 20 min break")
    elif REPS % 2 == 0:
        countdown_time = short_break_time
        label_10.config(text="Break", fg=PINK)
        messagebox.showinfo(title="times up", message="its time for a 5 min break")
    else:
        messagebox.showinfo(title="times up", message="its time to work")
        countdown_time = working_time
        CHECKMARK_COUNTER += 1
        checkmarks = ""
        for i in range(CHECKMARK_COUNTER):
            checkmarks += CHECKMARK
        label_13.config(text=checkmarks)
        label_10.config(text="Work", fg=GREEN)
    count_down(countdown_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    seconds = int(count % 60)
    minutes = int((count - seconds) / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)

label_10 = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
label_10.grid(column=1, row=0)

label_13 = Label(text="", font=(FONT_NAME, 16, "normal"), fg=GREEN, bg=YELLOW)
label_13.grid(column=1, row=3)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(f"{FONT_NAME}", 35, "bold"))
canvas.grid(column=1, row=1)

button_02 = Button(text="Start", command=start_timer)
button_02.grid(column=0, row=2)

button_22 = Button(text="Reset", command=reset)
button_22.grid(column=2, row=2)

window.mainloop()
