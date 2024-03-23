# pack() with parameter
# fill=X only fills in the x axis

from tkinter import *

root = Tk()

# frame one
frame1 = Frame(root,
               width=100,
               height=100,
               bg='blue')
# frame1.pack(fill=X)
frame1.pack(fill=Y)

# frame two
frame2 = Frame(root,
               width=50,
               height=50,
               bg='green')
# frame2.pack(fill=X)
frame2.pack(fill=Y)

# frame three
frame3 = Frame(root,
               width=25,
               height=25,
               bg='orange')
# frame3.pack(fill=X)
frame3.pack(fill=Y)

root.mainloop()