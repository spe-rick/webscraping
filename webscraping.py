from bs4 import BeautifulSoup
import requests

Pagetoscrape = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(Pagetoscrape.text, 'html.parser')
quotes = soup.find_all('span', attrs={"class": "text"})
authors = soup.findAll("small" , attrs={"class": "author"})

for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
