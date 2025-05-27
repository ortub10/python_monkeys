from tkinter import *

root = Tk()

root.geometry('600x400')

l1 = Label(root, text="Username")
l2 = Label(root, text="Password")

in1 = Entry(root)
in2 = Entry(root)

l1.grid(row=0, column=0, sticky=W)
l2.grid(row=1, column=0, sticky=W)

btn = Button(root, text="Send", width=10)

in1.grid(row=0, column=1, sticky=W, padx=4)
in2.grid(row=1, column=1, sticky=W, padx=4)

btn.grid(row=2, column=1, sticky=E, pady=8)

root.mainloop()
