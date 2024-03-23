# place()
# simple entry form

from tkinter import *

root = Tk()

root.geometry('400x250')

username = Label(root, text = 'Username', font = 'calibri 15 bold').place(x=30,y=50)
email = Label(root, text='Email', font = 'calibri 15 bold').place(x=30,y=90)
password = Label(root, text='Password', font = 'calibri 15 bold').place(x=30,y=130)

e1 = Entry(root).place(x=150,y=50)
e2 = Entry(root).place(x=150,y=90)
e3 = Entry(root).place(x=150,y=130)

root.mainloop()
