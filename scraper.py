import requests
from bs4 import BeautifulSoup
import pync
import datetime
import logging

# Set up logging
logging.basicConfig(filename='/Users/axilleas/Desktop/scraping/scraper.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Dictionary to map Greek month names to month numbers
months = {
    "Ιανουαρίου": 1,
    "Φεβρουαρίου": 2,
    "Μαρτίου": 3,
    "Απριλίου": 4,
    "Μαΐου": 5,
    "Ιουνίου": 6,
    "Ιουλίου": 7,
    "Αυγούστου": 8,
    "Σεπτεμβρίου": 9,
    "Οκτωβρίου": 10,
    "Νοεμβρίου": 11,
    "Δεκεμβρίου": 12
}

def date(dt):
    today = datetime.date.today()
    day, month_name, year = dt.split()
    month = months[month_name]
    article_date = datetime.date(int(year), month, int(day))
    return today == article_date

def get_articles():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    page = requests.get("https://www.unipi.gr/category/anakoinoseis-tmimatos-oikonomikis-epistimis/", headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all('article')
    for article in articles:
        date_str = article.find("span", class_="elementor-post-date").text.strip()
        if ('Αναβολή' in article.h2.text.strip() or "Πρόγραμμα" in article.h2.text.strip()) and date(date_str):
            titles = article.h2.text.strip()
            link = article.a['href']
            logging.info(f"Title: {titles}, Link: {link}")
            pync.notify(
                title="Νέα ανακοίνωση",
                message=titles,
                open=link,
                timeout=15
            )

if __name__ == "__main__":
    logging.info("Script started")
    get_articles()
    logging.info("Script finished")