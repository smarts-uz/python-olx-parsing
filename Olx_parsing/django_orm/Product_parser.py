import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.olx.uz/detskiy-mir/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Mahsulot linklarini olish
items = soup.find_all('a', class_='marginright5 link linkWithHash detailsLink')

for item in items:
    product_link = urljoin(url, item['href'])
    print(product_link)