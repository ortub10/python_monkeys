from tkinter import *

def on_red_click():
    myText.config(text="red", fg="red")

def on_blue_click():
    myText.config(text="blue", fg="blue")

root = Tk()
root.geometry("600x400")

root.title("my app")

myText = Label(root, text="This my app with buttons")
myText.pack()
myText.config(bg="yellow", font=("",32))

redBtn = Button(root, text="change to red", width=20, command=on_red_click)
redBtn.pack()

blueBtn = Button(root, text="change to blue", width=20, command=on_blue_click)
blueBtn.pack()

root.mainloop()
