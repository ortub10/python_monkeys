# This script defines a `Vod` class that represents a VOD (Video On Demand) item in a Tkinter GUI.

# Key Features:
# - Each VOD item displays a title, rating, release date, and a "More info" button.
# - When the button is clicked, a popup message box shows additional info about the VOD.
# - The `render()` method creates and packs the VOD item's GUI elements into a scrollable Canvas using
#   the `set_height()` function (imported from `scroller`) to vertically space the items.

# Dependencies:
# - Tkinter for GUI
# - A helper module named `scroller.py` that provides the `set_height` function

from tkinter import *

from scroller import set_height
from tkinter import messagebox

class Vod:
    def __init__(self, parent, title, rating, date, info):
        self.parent = parent
        self.title = title
        self.rating = rating
        self.date = date
        self.info = info

    def render(self):
        vod_frame = Frame(self.parent, borderwidth=1, relief="solid", padx=5, pady=5)

        title = Label(vod_frame, text=self.title, font=("", 20), width=20)
        title.pack()

        rating = Label(vod_frame, text=f"Rating:{self.rating}")
        rating.pack()

        date = Label(vod_frame, text=f"Release: {self.date}")
        date.pack()

        btn = Button(vod_frame, text="More info", command=self.on_btn_click)
        btn.pack()

        self.parent.create_window(10, set_height(130), anchor=NW, window=vod_frame)

    def on_btn_click(self):
        messagebox.showinfo("Info", self.info)
