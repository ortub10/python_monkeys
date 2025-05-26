from tkinter import *

def on_btn_click():
    print("click")
    
root = Tk()
root.geometry("600x400")

root.title("my app")

myText = Label(root, text="This my app with buttons")
myText.pack()

mtBtn = Button(root, text="click", width=25, command=on_btn_click)
mtBtn.pack()

root.mainloop()
