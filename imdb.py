import requests
import json
from bs4 import BeautifulSoup


def get_ld_json(url:str)->dict:
    querystring = {}
    headers = {
           "Accept": "application/json, text/plain, */*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
           "Referer": "https://www.imdb.com/"
    }
    response = requests.get(url, headers=headers, params=querystring)

    parser = "html.parser"
    soup = BeautifulSoup(response.text, parser)
    ## <script type="application/ld+json">
    return json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
    ##return response.text

def get_my_info(r):
    imdb_id = r.get("url").split("/")[-2]

    ## @type
    ## Movie | TVSeries

    print("imdb_id: "+imdb_id)
    return{

        "type": r.get('@type'),
        "name": r.get('name'),
        "url":  r.get('url'),
        "poster": r.get('image'),
        "description": r.get("description"),
        "genre": [genre for genre in r.get("genre", [])],
        "datePublished": r.get("datePublished"),


        "trailer_embedUrl":r.get("trailer").get("embedUrl"),

        "ratingValue": r.get("aggregateRating", {"ratingValue": None}).get("ratingValue"),

        "actor": [
                {"name": actor.get("name"), "url": actor.get("url")} for actor in r.get("actor", [])
            ],

        "director": [
                {"name": director.get("name"), "url": director.get("url")} for director in r.get("director", [])
            ],
               
          }



print(
    get_my_info( get_ld_json("https://www.imdb.com/title/tt0068646/") )
)



