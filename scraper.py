import requests
from bs4 import BeautifulSoup
import pync

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
page = requests.get("https://www.unipi.gr/category/anakoinoseis-tmimatos-oikonomikis-epistimis/", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


articles = soup.find_all('article')
for article in articles:
    if 'Αναβολή' in article.h2.text.strip() or "Πρόγραμμα" in article.h2.text.strip():
        titles = article.h2.text.strip()
        print(titles)
        link = article.a['href']
        print(link + '\n')
        pync.notify(
            title = "Νέα ανακοίνωση",
            message = titles,
            open = link,
            timeout=15
        )