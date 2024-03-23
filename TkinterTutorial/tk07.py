# pack() with parameter
# side and expand

from tkinter import *

root = Tk()

# frame one
frame1 = Frame(root,
               width=100,
               height=100,
               bg='blue')
frame1.pack(fill=BOTH, side=LEFT, expand=True)


# frame two
frame2 = Frame(root,
               width=50,
               height=50,
               bg='green')
frame2.pack(fill=BOTH, side=LEFT, expand=True)


# frame three
frame3 = Frame(root,
               width=25,
               height=25,
               bg='orange')
frame3.pack(fill=BOTH, side=LEFT, expand=True)


root.mainloop()