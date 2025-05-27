from tkinter import *

def on_btn_click():
    myText2.config(text="Color is: " + myInput1.get())

root = Tk()
root.geometry("600x400")

root.title("my app")

myText1 = Label(root, text="Choose your favorite color: ", font=("", 18))
myText1.pack()

myInput1 = Entry(root, width=20, font=("", 16))
myInput1.pack(pady=16)

btn = Button(root, text="change", font=("", 16), command=on_btn_click)
btn.pack()

myText2 = Label(root, text="Color is:", font=("", 18))
myText2.pack()

root.mainloop()
