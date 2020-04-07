from time import strftime
from tkinter import *
clock_frame =Tk()

Label(clock_frame,text=strftime("%H:%M:%S"),fg="light green",bg="black",font="Helvetica 120 bold")
res = Label(clock_frame)
res.pack()
def display():
    res.configure(text=strftime("%H:%M:%S"))
def repeat():
    display()
    clock_frame.after(500,repeat)
repeat()
