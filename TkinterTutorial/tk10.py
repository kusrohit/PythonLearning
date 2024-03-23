# Label()

from tkinter import *

root = Tk()
root.geometry('600x400')

var = StringVar()
label = Label(root,
              textvariable=var,
              relief=RAISED)

var.set('Welcome to tkinter !!')

label.pack()
root.mainloop()