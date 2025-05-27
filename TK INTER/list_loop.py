from tkinter import *

root = Tk()
colors_list = ["blue", "red", "green", "yellow"]
cars_list = ["mazda", "bmw", "opel", "toyota"]

root.geometry('600x400')

for i in range(len(colors_list)):
    myBtn = Button(root, text=cars_list[i])
    myBtn.config(width=25, bg=colors_list[i])
    myBtn.pack()

for c in colors_list:
    myBtn = Button(root, text=c)
    myBtn.config(width=25, bg=c)
    myBtn.pack()

root.mainloop()
