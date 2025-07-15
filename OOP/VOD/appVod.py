# This script creates a simple graphical VOD (Video on Demand) application using Tkinter in Python.
#
# Specifically:
# - It fetches a list of movies or TV shows using the `get_api_data` function from an external API (TMDb).
# - Each media item (title, rating, release date, and overview) is displayed in a scrollable Tkinter canvas,
#   using a custom `Vod` class to handle rendering of each entry.
# - A vertical scrollbar is added to the canvas to allow navigation through multiple entries.
# - The GUI window is initialized with a title and size, and the main event loop is started.
#
# Requirements:
# - The modules `vodClass`, `vodApi`, and `scroller` must be implemented and available.
# - Internet access is required to fetch the movie data from the API.

from vodClass import *
from vodApi import get_api_data
from scroller import add_scrollbar
root = Tk()

def init():
    create_movie()
    create_ui_tk()


def create_movie():
    global root
    lst = get_api_data()
    canvas = Canvas(root, width=550)
    for item in lst:
        video = Vod(canvas, item["title"], item["vote_average"], item["release_date"], item["overview"])
        video.render()

    add_scrollbar(root, canvas)
def create_ui_tk():
    root.geometry('600x400')
    root.title("vod app")
    root.mainloop()

init()
