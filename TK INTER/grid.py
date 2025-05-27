from tkinter import *

root = Tk()

root.geometry('600x400')

l1 = Label(root, text="first", borderwidth=1, relief="solid")
l2 = Label(root, text="second", borderwidth=1, relief="solid")
l3 = Label(root, text="third", borderwidth=1, relief="solid")

l1.grid(row=0, column=0, sticky=W)
l2.grid(row=1, column=0)
l3.grid(row=0, column=1)

root.mainloop()
