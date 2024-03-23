from tkinter import *

root = Tk()
root.geometry('400x250')

username = Label(root,
             text='Username').place(x=30,y=50)
password = Label(root,
                 text='Password').place(x=30,y=90)
submit_btn = Button(root,
                    text='Submit',
                    activebackground='red',
                    activeforeground='blue').place(x=30,y=120)

e1 = Entry(root,width=20).place(x=100,y=50)
e2 = Entry(root,width=20).place(x=100,y=90)

root.mainloop()