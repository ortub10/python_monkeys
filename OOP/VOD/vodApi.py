# This script defines a function that retrieves a list of movies or TV shows
# from a specific list on The Movie Database (TMDb) using their public API.

# Specifically:
# - It sends a GET request to TMDb's API to fetch the contents of list ID 3.
# - It uses an API key to authenticate the request.
# - It returns only the 'items' part of the JSON response, which contains the actual media entries.

# Note: You need an active internet connection and the `requests` library installed for this to work.


import requests
def get_api_data():
    url = "https://api.themoviedb.org/3/list/3?api_key=d4bc3c640586e7f90dc68d8b300247ff&language=en-US"
    resp = requests.get(url)
    json = resp.json()
    return json["items"]
