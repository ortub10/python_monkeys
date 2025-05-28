# This is a simple shopping list GUI application built using Tkinter.
# Users can add product names to the shopping list, view the current list,
# and reset (clear) the entire list. The interface includes:
# - An entry box to type in product names
# - A button to add the product to the list
# - A button to reset the list
# - A section displaying the list of added products

from tkinter import *

root = Tk()

valInput = btnAdd = list_frame = ""

shopList = []

def create_list():
    global list_frame
    list_frame = Frame(root)
    list_frame.grid(column=0, sticky=W, pady=20)

    for i in shopList:
        item = Label(list_frame, text=i, borderwidth=1, relief="solid", padx=5, width=30, anchor=W)
        item.pack()

def on_reset():
    global shopList
    global list_frame
    shopList = []
    list_frame.destroy()


def on_btn_add():
    global shopList
    global list_frame
    list_frame.destroy()
    shopList.append(valInput.get())
    valInput.delete(0, END)
    create_list()

def create_gui():
    global valInput
    global btnAdd

    root.geometry('600x400')
    root.title("shops list")

    title = Label(root, text="Shopping app", font=("", 24))
    title.grid(row=0, column=0, sticky=W)

    label = Label(root, text="Product name:")
    label.grid(row=1, column=0, sticky=W)

    valInput = Entry(root, width=20)
    valInput.grid(row=2, column=0, sticky=W)

    btnAdd = Button(root, text="Add product", command=on_btn_add, width=25)
    btnAdd.grid(row=3, column=0, sticky=W)

    reset_btn = Button(root, text="reset list", command=on_reset, width=25)
    reset_btn.grid(row=4, column=0, sticky=W)

    label_item_add = Label(list_frame, text="Product you added:", padx=5, width=30, anchor=W)
    label_item_add.grid(row=5, column=0, sticky=W)

create_gui()
create_list()
root.mainloop()
