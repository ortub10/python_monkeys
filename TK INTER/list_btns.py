# This simple Tkinter application displays a list of letters one at a time.
# The user can navigate forward and backward through the list using "next" and "back" buttons.
# The currently selected letter is shown in a large font at the top of the window

from tkinter import *

root = Tk()

lettersList = ["a", "b", "c", "d", "e", "f"]
index = 0

def update_ui():
    myText.config(text=lettersList[index])

def on_btn_next():
    global index
    index += 1
    if index > len(lettersList) - 1:
        index = 0
    update_ui()
    
def on_btn_back():
    global index
    index -= 1
    if index < 0:
        index = len(lettersList) - 1
    update_ui()

root.geometry('600x400')
root.grid_columnconfigure(0, weight=1)


myText = Label(root, text="a", font=("", 24))
frameButtons = Frame(root)

btnBack = Button(root, text="back", command=on_btn_back)
btnNext = Button(root, text="next", command=on_btn_next)

myText.grid(row=0, column=0, pady=8)
frameButtons.grid(row=1, column=0)
btnBack.grid(row=0, column=0)
btnNext.grid(row=0, column=1)


root.mainloop()

