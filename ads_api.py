
from bs4 import BeautifulSoup
import requests
import lxml


headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582",
}

html = requests.get(
    'https://www.google.com/search?q=graphic+card+buy&oq=graphic+\
    card+buy&hl=en&gl=us&sourceid=chrome&ie=UTF-8',
    headers=headers).text


soup = BeautifulSoup(html, 'lxml')

for link in soup.findAll('div', class_=''):
    ad_link = link.a['href']
    print(f'https://www.googleadservices.com/pagead{ad_link}')
