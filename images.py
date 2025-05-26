from tkinter import *

def resize_image(image, new_width, new_height):
    old_width = image.width()
    old_height = image.height()
    new_photo_image = PhotoImage(width=new_width, height=new_height)
    for x in range(new_width):
        for y in range(new_height):
            x_old = int(x*old_width/new_width)
            y_old = int(y*old_height/new_height)
            rgb = '#%02x%02x%02x' % image.get(x_old, y_old)
            new_photo_image.put(rgb, (x, y))
    return new_photo_image

def on_input(_):
    myText.config(text=myInput.get())

root = Tk()
root.geometry('600x400')


imgUrl = PhotoImage(file="images/python3.png")
imgUrl = resize_image(imgUrl, 200, 100)
img = Label(root, image=imgUrl)
img.pack()

myInput = Entry(root, width=20, font=("", 16))
myInput.bind("<KeyRelease>", on_input)
myInput.pack()

myText = Label(root, font=("", 16))
myText.pack()

root.mainloop()
