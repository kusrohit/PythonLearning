# adding stryle and event handler to btn

from tkinter import *
from tkinter import messagebox as msb


root = Tk()
root.geometry('300x150')

def click():
    msb.showinfo('Hello', 'Green Button clicked')

a = Button(root, text='yellow', activebackground='yellow', activeforeground='orange')

root.mainloop()

