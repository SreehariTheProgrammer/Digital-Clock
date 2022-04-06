import time
from tkinter import *

root = Tk()
root.configure(background="black")
root.title("Clock")

def start():
    text = time.strftime("%H:%M:%S")
    Label.config(text=text)
    Label.after(200, start)

Label = Label(root, font=("DS-Digital", 100), fg="green", bg="black", bd=50)
Label.grid(row=0, column=50)
start()
root.mainloop()