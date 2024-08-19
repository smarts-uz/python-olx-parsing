import requests
from bs4 import BeautifulSoup
import time

from Parsing.orm.db.models import Category
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()
#

def fetch_and_parse_categories():
    url = "https://www.olx.uz/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # HTML tuzilmasini tekshirib, kategoriya linklarini topish
    category_items = soup.find_all('a', class_='css-1ep67ka')  # To'g'ri class nomini qo'shish

    category_list = []

    for item in category_items:
        name_tag = item.find('p', class_='css-g6otoa')
        name = name_tag.get_text(strip=True) if name_tag else 'No Name'
        category_url = item['href']
        if category_url.startswith('/'):
            category_url = "https://www.olx.uz" + category_url

        category_list.append({'name': name, 'url': category_url})
        obj = Category(name=name, category_url=category_url)
        obj.save()
    # Print the list of categories
    print(category_list)

    # Pause between requests to avoid being blocked
    time.sleep(1)


# Call the function
fetch_and_parse_categories()


#
#

# class Command(BaseCommand):
#     help = 'Fetch and parse OLX categories'
#
#     def handle(self, *args, **kwargs):
#         self.fetch_and_parse_categories()
#
#     def fetch_and_parse_categories(self):
#         url = "https://www.olx.uz/"
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # HTML tuzilmasini tekshirib, kategoriya linklarini topish
#         category_items = soup.find_all('a', class_='css-1ep67ka')  # To'g'ri class nomini qo'shish
#
#         for item in category_items:
#             name_tag = item.find('p', class_='css-g6otoa')
#             name = name_tag.get_text(strip=True) if name_tag else 'No Name'
#             category_url = item['href']
#             if category_url.startswith('/'):
#                 category_url = "https://www.olx.uz" + category_url
#
#             # # Bazaga saqlash
#             # Category.objects.update_or_create(
#             #     name=name,
#             #     defaults={'category_url': category_url}
#             # )
#             obj=Category(name=name,category_url=category_url)
#             obj.save()
#
#         # Pause between requests to avoid being blocked
#         time.sleep(1)