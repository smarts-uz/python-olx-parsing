import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import click
import django
import argparse
from one_Product_parser import get_product_details, download_image
from dotenv  import load_dotenv

load_dotenv()  # Load environment variables from .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')  # Ensure this is correct
django.setup()

from parserapp.models import Category, Moda_stil, Bolalar_dunyosi, Kochmas_mulk, Transport, Ish, Hayvonlar, Uy_va_Bog, Elektronika, Biznes_va_Xizmatlar, Xobbi_va_Sport, Tekinga_berish, Ayirboshlash

def get_product_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='css-1ut25fa')

    if not items:
        print("No items found. Please check the class names or the HTML structure.")
        return []

    product_links = []
    for item in items:
        link_tag = item.find('a', class_='css-z3gu2d')
        if link_tag and 'href' in link_tag.attrs:
            product_link = urljoin(url, link_tag['href'])
            product_links.append(product_link)

    return product_links

def get_all_product_links(start_url):
    all_product_links = []
    url = start_url

    while url:
        product_links = get_product_links(url)
        all_product_links.extend(product_links)

        # Find next page URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_page_tag = soup.find('a', {'data-cy': 'pagination-forward'})

        if next_page_tag and 'href' in next_page_tag.attrs:
            url = urljoin(start_url, next_page_tag['href'])
        else:
            url = None

        # 1-soniyalik pauza
        time.sleep(1)

    return all_product_links

def get_model_class(model_name):
    model_mapping = {
        'Moda_stil': Moda_stil,
        'Bolalar_dunyosi': Bolalar_dunyosi,
        'Kochmas_mulk': Kochmas_mulk,
        'Transport': Transport,
        'Ish': Ish,
        'Hayvonlar': Hayvonlar,
        'Uy_va_Bog': Uy_va_Bog,
        'Elektronika': Elektronika,
        'Biznes_va_Xizmatlar': Biznes_va_Xizmatlar,
        'Xobbi_va_Sport': Xobbi_va_Sport,
        'Tekinga_berish': Tekinga_berish,
        'Ayirboshlash': Ayirboshlash,
    }
    return model_mapping.get(model_name)

@click.command()
@click.argument('category_id', type=int)
def main(category_id):
    """Kategoriya URL'dan mahsulot havolalarini olish."""
    try:
        category = Category.objects.get(id=category_id)
        start_url = category.category_url
        model_name = category.model_name
    except Category.DoesNotExist:
        print(f"ID {category_id} bo'yicha kategoriya mavjud emas.")
        return

    category_model = get_model_class(model_name)
    if not category_model:
        print(f"{model_name} nomli model mavjud emas.")
        return

    all_product_links = get_all_product_links(start_url)

    if all_product_links:
        for link in all_product_links:
            print(link)
            product_details = get_product_details(link, category_model)
            print(product_details)
            # download_image(product_details['product_image_path'], product_details['product_name'])  # To'g'ri parametrlar

    else:
        print("Hech qanday mahsulot havolalari topilmadi.")

if __name__ == "__main__":
    main()