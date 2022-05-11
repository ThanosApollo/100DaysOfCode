from isort import file
import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text 
print(yc_web_page)


soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(class_='article-title-description__text')

movies = []

for movie in articles:
    movies.append(movie.h3.getText())

print(movies)

with open('top100Movies.txt', 'w') as file : 
    for movie in movies[::-1] :
        file.write(movie)
        file.write('\n')

