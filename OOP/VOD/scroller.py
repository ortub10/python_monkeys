# This script provides utility functions to work with a scrollable `Canvas` widget in Tkinter.

# Features:
# - A `set_height(px)` function that dynamically increases height values based on how many times it's called.
#   Useful for positioning or sizing elements with consistent vertical spacing.
# - An `add_scrollbar(root, the_canvas)` function that adds a vertical scrollbar to a given Canvas widget,
#   enabling vertical scrolling of its content.

# Note: Requires the Tkinter GUI library.

from tkinter import *
counter = 0
def set_height(px):
    global counter
    counter += 1
    return 10 + (px * counter)

def add_scrollbar(root, the_canvas):
    scrollbar = Scrollbar(root)
    the_canvas.pack(side=LEFT, fill=BOTH)
    the_canvas.config(scrollregion=the_canvas.bbox("all"))
    the_canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=the_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
