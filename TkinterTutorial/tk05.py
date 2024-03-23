# pack()
# pack() method stack every frame in middle of the parent window

from tkinter import *

root = Tk()

# frame one
frame1 = Frame(root,
               width=100,
               height=100,
               bg='blue')
frame1.pack()

# frame two
frame2 = Frame(root,
               width=50,
               height=50,
               bg='green')
frame2.pack()

# frame three
frame3 = Frame(root,
               width=25,
               height=25,
               bg='orange')
frame3.pack()

root.mainloop()
