from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

label = Label(
    root, font=("sans-serf", 100),
    background="black",
    foreground="white"
)

# define Time that use in Clock Appliciation


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label.pack(anchor="center")

# Start Clock

time()
mainloop()
