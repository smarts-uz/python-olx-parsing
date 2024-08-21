import requests
from bs4 import BeautifulSoup
import time
import django
import os
from dotenv import load_dotenv

# Django muhitini sozlash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
django.setup()

from parserapp.models import Category

# .env faylni yuklash
load_dotenv()

# Asosiy URL
base_url = "https://www.olx.uz"

def fetch_and_parse_categories():
    # OLX bosh sahifasidan kategoriyalarni olish
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Har xil class'lar uchun HTML tuzilmasini tekshirish va kategoriya linklarini topish
    category_items = soup.find_all('a', class_='css-1ep67ka') + soup.find_all('a', class_='css-60fzsg')

    category_list = []
    i = 0
    for item in category_items:
        name_tag = item.find('p', class_='css-g6otoa')
        name = name_tag.get_text(strip=True) if name_tag else 'No Name'
        category_url = item['href']

        if category_url.startswith('/'):
            category_url = base_url + category_url

        category_list.append({'name': name, 'url': category_url})

        # Ma'lumotlar bazasida kategoriya mavjudligini tekshirish va saqlash
        try:
            Category.objects.get(category_name=name)
            print(f'Category "{name}" already exists with Category_link: {category_url}')
        except Category.DoesNotExist:
            Category.objects.create(
                category_name=name,
                category_url=category_url
            )
            i += 1
            print(i, 'created:', name)

        # Kategoriya haqida ma'lumotni chop etish
        print(f"\n{name} with Category_link: {category_url} parsing finished")

    # Kategoriyalar ro'yxatini chop etish
    print(category_list)

    # Bloklanmaslik uchun so'rovlar orasida pauza qilish
    time.sleep(1)

# Funksiyani chaqirish
fetch_and_parse_categories()