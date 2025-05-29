# This module defines a FoodClass used in a simple food menu GUI application built with Tkinter.
# Each instance of the class represents a food item with a name and a price.
# The class handles:
# - Creating a button in the main window for the food item
# - Displaying a popup message with the price when the button is clicked

from tkinter import *
from tkinter import messagebox

class FoodClass:
    def __init__(self, root,  name, price):
        self.root = root
        self.name = name
        self.price = price

    def add_to_ui(self):
        btn = Button(self.root, text=self.name, command=self.on_btn_click)
        btn.grid(column=0, sticky=W)

    def on_btn_click(self):
        messagebox.showinfo("Price is", f"{self.price} NIS")
