import requests
import os
from auth import API_KEY



BASE_URL= "https://api.themoviedb.org/3/trending/movie/week"
API=API_KEY

query_params={
    "api_key":API
}

response = requests.get(BASE_URL, params=query_params)

movies=response.json()["results"]
for movie in movies[0:10]:
    print(movie["title"])