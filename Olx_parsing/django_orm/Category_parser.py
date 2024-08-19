import requests
from bs4 import BeautifulSoup
import time
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
django.setup()

from parserapp import models
from parserapp.models import Category
import os
from dotenv import load_dotenv
import django


def fetch_and_parse_categories():
    url = "https://www.olx.uz/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # HTML tuzilmasini tekshirib, kategoriya linklarini topish
    category_items = soup.find_all('a', class_='css-1ep67ka')  # To'g'ri class nomini qo'shish

    category_list = []
    i=0
    for item in category_items:
        name_tag = item.find('p', class_='css-g6otoa')
        name = name_tag.get_text(strip=True) if name_tag else 'No Name'
        category_url = item['href']
        if category_url.startswith('/'):
            category_url = "https://www.olx.uz" + category_url

        category_list.append({'name': name, 'url': category_url})
        try:
            Category.objects.get(category_name=name)
            print(f'Category {name} already exists with Category_link:{category_url}')
        except Category.DoesNotExist:
            Category.objects.create(
                category_name=name,
                category_url=category_url
            )
            i += 1
            print(i, 'created:', name)

        print(f"\n{name}  with Category_link:{category_url} parsing finished")
    # Print the list of categories
    print(category_list)

    # Pause between requests to avoid being blocked
    time.sleep(1)


# Call the function
fetch_and_parse_categories()

