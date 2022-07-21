import requests
import bs4
import re
from fake_headers import Headers


HEADERS = Headers(
        # browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()

BASE_URL = "https://habr.com"
add_url = "/ru/all"

KEYWORDS = {'Чаще', 'дизайн', 'фото', 'web', 'python'}


response = requests.get(BASE_URL + add_url, headers=HEADERS)
text = response.text
# print(text)

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    preview = article.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-1")
    if preview is not None:
        if len(KEYWORDS.intersection(set(re.findall(r'\w*', preview.text)))) != 0:
            date_time = article.find('time').attrs['datetime']
            head = article.find('h2').find('a').text
            link = BASE_URL + article.find('h2').find('a').attrs['href']
            print(f'{date_time} - {head} - {link}\n\n')
