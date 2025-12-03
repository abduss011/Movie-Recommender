import requests
import re

def get_details(title, api_key, year=None):
    clean_title = re.sub(r'[^a-zA-Z0-9 ]', '', title)
    clean_title = clean_title.replace(' ', '+')
    url = f"http://www.omdbapi.com/?t={clean_title}&apikey={api_key}"
    if year:
        url += f"&y={year}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        plot = res.get("Plot", "N/A")
        poster = res.get("Poster", "N/A")
        return plot, poster
    search_url = f"http://www.omdbapi.com/?s={clean_title}&apikey={api_key}"
    if year:
        search_url += f"&y={year}"
    search_res = requests.get(search_url).json()
    if search_res.get("Response") == "True" and search_res.get("Search"):
        first_result = search_res["Search"][0]
        imdb_id = first_result["imdbID"]
        details_url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
        details_res = requests.get(details_url).json()
        plot = details_res.get("Plot", "N/A")
        poster = details_res.get("Poster", "N/A")
        return plot, poster
    return "N/A", "N/A"
