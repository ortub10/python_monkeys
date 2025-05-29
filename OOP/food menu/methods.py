# This is the main script for a simple food menu GUI application built using Tkinter.
# It uses the FoodClass to represent different food items.
# The interface includes:
# - A title label at the top
# - Buttons for each food item (e.g., Pizza, Burger)
# - When a button is clicked, it shows the price of that item in a popup message

from tkinter import *
from FoodClass import FoodClass

root = Tk()

def main():
    create_title()
    create_food()
    create_root_ui()

def create_title():
    title = Label(root, text="Food menu", font=("", 22))
    title.grid(column=0, sticky=W)

def create_food():
    food1 = FoodClass(root, "Pizza", 24)
    food2 = FoodClass(root, "Burger", 35)
    food1.add_to_ui()
    food2.add_to_ui()

def create_root_ui():
    root.geometry('600x400')
    root.mainloop()


if __name__ == '__main__':
    main()
