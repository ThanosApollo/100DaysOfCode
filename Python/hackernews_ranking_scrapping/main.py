from urllib import response
from bs4 import BeautifulSoup
import requests
 

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name='a', class_='titlelink')

article_texts = []
article_links = []

for article_tag in articles: 
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_link = article_tag.get('href')
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_upvote = max(article_upvotes)
index = article_upvotes.index(largest_upvote)
print(article_links[index])
print(article_texts[index])

