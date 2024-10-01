import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
page = requests.get("https://www.unipi.gr/category/anakoinoseis-tmimatos-oikonomikis-epistimis/", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


articles = soup.find_all('article')
for article in articles:
    titles = article.h2.text.strip()
    print(titles)
    link = article.a['href']
    print(link + '\n')