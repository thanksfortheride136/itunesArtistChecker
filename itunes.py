#NOTE: You must run the program as usual: python3 itunes.py. Search Terms are case sensitive.

import requests
import json

print("Program Running...")

search_term = input("Enter a search term: ")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + search_term) #makes api request to itunes, can specify number of results in limit parameter

o = response.json()
for result in o["results"]:
    print(result["trackName"])