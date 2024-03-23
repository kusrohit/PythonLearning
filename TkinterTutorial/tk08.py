# grid(options)

from tkinter import *

root = Tk()

for i in range(10):
    for j in range(10):
        frame = Frame(root,
                      relief=RAISED,
                      borderwidth=1)

        # frame.grid(row=i,column=j)
        frame.grid(row=i,column=j,padx=10,pady=10)
        label = Label(frame,text=f'Row {i}\nColumn {j}')
        label.pack()
        
root.mainloop()