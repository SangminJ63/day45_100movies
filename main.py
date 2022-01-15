import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text
soup = BeautifulSoup(movies_web_page, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
movie_list = [movie.string for movie in movie_titles]
movies = movie_list[::-1]

for movie in movies:
    print(movie)

with open("movies.txt", mode="w", encoding="UTF8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
